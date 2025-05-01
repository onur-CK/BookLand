import json
import time
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import Order, OrderLineItem
from products.models import Book
from profiles.models import UserProfile


class StripeWH_Handler:
    """
    Handle Stripe webhooks
    Source: https://stripe.com/docs/webhooks
    """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        customer_email = order.email
        subject = f'BookLand - Order Confirmation {order.order_number}'
        
        # Render email templates to strings
        html_message = render_to_string(
            'checkout/confirmation_email/confirmation_email_body.html',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )
        
        # Create plain text version
        plain_message = strip_tags(html_message)
        
        # Send email
        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email],
            html_message=html_message
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        Source: https://stripe.com/docs/webhooks/signatures
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        Source: https://stripe.com/docs/payments/payment-intents/verifying-status
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        # Get the Charge object to access billing/shipping details
        stripe_charge = intent.latest_charge
        
        billing_details = intent.shipping
        shipping_details = intent.shipping

        # Clean data in shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_street_address = shipping_details.address.line1
                profile.default_apartment = shipping_details.address.line2
                profile.default_city = shipping_details.address.city
                profile.default_postal_code = shipping_details.address.postal_code
                profile.default_country = shipping_details.address.country
                profile.save()

        # Check if order exists already
        order_exists = False
        attempt = 1
        
        # Sometimes the form submission view creates the order before the webhook
        # This handles the race condition by checking a few times before creating a new order
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    street_address__iexact=shipping_details.address.line1,
                    apartment__iexact=shipping_details.address.line2,
                    city__iexact=shipping_details.address.city,
                    postal_code__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                    grand_total=intent.amount_received / 100,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        # If order exists, return success response
        if order_exists:
            # Send confirmation email
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            # Create new order if it doesn't exist in our database
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    street_address=shipping_details.address.line1,
                    apartment=shipping_details.address.line2,
                    city=shipping_details.address.city,
                    postal_code=shipping_details.address.postal_code,
                    country=shipping_details.address.country,
                )
                
                # Convert JSON string to Python dictionary
                cart_dict = json.loads(cart)
                
                # Create order line items
                for item_id, quantity in cart_dict.items():
                    book = Book.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        book=book,
                        quantity=quantity,
                    )
                    order_line_item.save()
            except Exception as e:
                # If anything goes wrong, delete the order if it was created
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        # Send confirmation email
        self._send_confirmation_email(order)
        
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        Source: https://stripe.com/docs/payments/handling-payment-events
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
    

