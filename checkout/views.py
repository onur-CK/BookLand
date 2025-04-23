# Source: https://docs.djangoproject.com/en/5.1/topics/http/views/
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Book
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from cart.contexts import cart_contents
from decimal import Decimal

def checkout(request):
    """
    Handle the checkout process with dynamic shipping cost
    Source: https://docs.djangoproject.com/en/5.1/topics/forms/
    """
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
            # Calculate total and shipping
            current_cart = cart_contents(request)
            total = current_cart['total']
            
            # Determine shipping cost - free if order >= $40
            shipping_cost = Decimal('0.00') if total >= 40 else Decimal('5.00')
            
            # Save the order with calculated shipping
            order = order_form.save(commit=False)  # Don't save to DB yet
            order.shipping_cost = shipping_cost
            order.order_total = total
            order.grand_total = total + shipping_cost
            order.save()  # Now save to DB

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
    }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts - shows order confirmation
    Source: https://docs.djangoproject.com/en/5.1/topics/db/queries/#retrieving-a-single-object-with-get
    """
    # Get save_info preference from session
    save_info = request.session.get('save_info')
    
    # Get the order that was just created
    order = get_object_or_404(Order, order_number=order_number)

    # If user is logged in, attach order to their profile
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        # Save the shipping info to user profile if requested
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_street_address': order.street_address,
                'default_apartment': order.apartment,
                'default_city': order.city,
                'default_postal_code': order.postal_code,
                'default_country': order.country,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    # Show success message to user
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    # Clear the cart now that checkout is complete
    if 'cart' in request.session:
        del request.session['cart']

    # Prepare context for the template
    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)