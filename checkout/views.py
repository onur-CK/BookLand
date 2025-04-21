# checkout/views.py
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Book
from profiles.models import UserProfile
from cart.contexts import cart_contents

def checkout(request):
    """
    Handle the checkout process
    """
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    if request.method == 'POST':
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
            order = order_form.save()
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
                    messages.error(request, "One of the books in your cart wasn't found in our database.")
                    order.delete()
                    return redirect(reverse('view_cart'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')
    else:
        order_form = OrderForm()

    current_cart = cart_contents(request)
    context = {
        'order_form': order_form,
        'cart_items': current_cart['cart_items'],
        'total': current_cart['total'],
        'product_count': current_cart['product_count'],
        'shipping': current_cart['shipping'],
        'grand_total': current_cart['grand_total'],
    }

    return render(request, 'checkout/checkout.html', context)