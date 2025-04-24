import json
import stripe
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Book
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from cart.contexts import cart_contents
from decimal import Decimal

@require_POST
def cache_checkout_data(request):
    """
    Cache checkout data in the Stripe Payment Intent metadata before payment is confirmed
    Source: https://stripe.com/docs/payments/payment-intents
    """
    try:
        # Get the payment intent ID from the POST data
        pid = request.POST.get('client_secret').split('_secret')[0]
        # Set up Stripe with the secret key
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # Modify the payment intent to add metadata
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user.username if request.user.is_authenticated else 'AnonymousUser',
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Sorry, your payment cannot be processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

def checkout(request):
    """
    Handle the checkout process and integrate with Stripe for payment
    Source: https://stripe.com/docs/payments/accept-a-payment
    """
    # Set up Stripe keys from settings
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    # Get the current cart from session
    cart = request.session.get('cart', {})
    
    # Redirect if cart is empty
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    if request.method == 'POST':
        # Process the form data when form is submitted
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address': request.POST['street_address'],
            'apartment': request.POST['apartment'],
            'city': request.POST['city'],
            'postal_code': request.POST['postal_code'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        
        if order_form.is_valid():
            # Save the order but prevent immediate database commit
            order = order_form.save(commit=False)
            
            # Get payment intent ID from client secret if it exists
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            
            # Calculate total and shipping
            current_cart = cart_contents(request)
            total = current_cart['total']
            
            # Determine shipping cost - free if order >= $40
            shipping_cost = Decimal('0.00') if total >= 40 else Decimal('5.00')
            
            # Save shipping cost to order
            order.shipping_cost = shipping_cost
            order.order_total = total
            order.grand_total = total + shipping_cost
            order.save()

            # Create order line items for each product in cart
            for item_id, quantity in cart.items():
                try:
                    book = Book.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        book=book,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Book.DoesNotExist:
                    # Handle case where book isn't found
                    messages.error(request, "One of the books in your cart wasn't found in our database.")
                    order.delete()  # Delete the order to prevent incomplete orders
                    return redirect(reverse('view_cart'))

            # Record if user wants to save their info for next time
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            # Form is invalid - show error message
            messages.error(request, 'There was an error with your form. Please double check your information.')
    else:
        # GET request - display empty form
        order_form = OrderForm()

    # Calculate cart contents and shipping for display
    current_cart = cart_contents(request)
    total = current_cart['total']
    
    # Determine shipping cost for display
    shipping_cost = Decimal('0.00') if total >= 40 else Decimal('5.00')
    grand_total = total + shipping_cost
    
    # Create Stripe payment intent
    if grand_total > 0:
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=int(grand_total * 100),  # Convert to cents
            currency=settings.STRIPE_CURRENCY,
            payment_method_types=['card'],
        )
        client_secret = intent.client_secret
    else:
        # Handle 0 value cart
        stripe_public_key = ''
        client_secret = ''

    # Check if Stripe keys are set
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you set it in your environment variables?')

    # Context data for the template
    context = {
        'order_form': order_form,
        'cart_items': current_cart['cart_items'],
        'total': total,
        'product_count': current_cart['product_count'],
        'shipping': shipping_cost,
        'grand_total': grand_total,
        'free_shipping_threshold': 40,
        'remaining_for_free_shipping': max(0, Decimal('40.00') - total),
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret,
    }

    return render(request, 'checkout/checkout.html', context)