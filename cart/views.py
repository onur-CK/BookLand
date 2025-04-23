from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from products.models import Book

def view_cart(request):
    """
    A view to return the shopping cart page
    Source: https://docs.djangoproject.com/en/5.1/topics/http/views/
    """
    # Simply render the cart template - context processor adds cart data
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """
    Add a quantity of the specified product to the shopping cart
    Source: https://docs.djangoproject.com/en/5.1/topics/http/sessions/
    """
    # Get the book object from database
    book = get_object_or_404(Book, pk=item_id)
    # Get the quantity from the form (default to 1 if not specified)
    quantity = int(request.POST.get('quantity', 1))
    # Get the URL to redirect back to after processing
    redirect_url = request.POST.get('redirect_url')
    # Get the current cart from session or create empty dict
    cart = request.session.get('cart', {})

    # Update quantity if the item is already in the cart
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {book.title} quantity to {cart[item_id]}')
    # Otherwise add the item to the cart
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {book.title} to your cart')

    # Save the updated cart back to the session
    request.session['cart'] = cart
    # Redirect back to the previous page
    return redirect(redirect_url)

def adjust_cart(request, item_id):
    """
    Adjust the quantity of the specified product to the specified amount
    Source: https://docs.djangoproject.com/en/5.1/topics/http/sessions/
    """
    # Get the book object from database
    book = get_object_or_404(Book, pk=item_id)
    # Get the new quantity from the form
    quantity = int(request.POST.get('quantity'))
    # Get the current cart from session
    cart = request.session.get('cart', {})

    # If quantity is positive, update the item quantity
    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {book.title} quantity to {cart[item_id]}')
    # If quantity is zero or negative, remove the item completely
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {book.title} from your cart')

    # Save the updated cart back to the session
    request.session['cart'] = cart
    # Redirect to the cart page
    return redirect(reverse('view_cart'))

def remove_from_cart(request, item_id):
    """
    Remove the item from the shopping cart
    Source: https://docs.djangoproject.com/en/5.1/topics/http/sessions/
    """
    try:
        # Get the book object from database
        book = get_object_or_404(Book, pk=item_id)
        # Get the current cart from session
        cart = request.session.get('cart', {})

        # Remove the item from the cart
        cart.pop(item_id)
        messages.success(request, f'Removed {book.title} from your cart')

        # Save the updated cart back to the session
        request.session['cart'] = cart
        return redirect(reverse('view_cart'))
    except Exception as e:
        # Handle any errors that occur during the process
        messages.error(request, f'Error removing item: {e}')
        return redirect(reverse('view_cart'))