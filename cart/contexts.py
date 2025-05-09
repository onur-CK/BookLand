from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Book


def cart_contents(request):
    """
    Context processor to make cart contents available across all templates
    Source: https://docs.djangoproject.com/en/5.1/ref/templates/api/#writing-your-own-context-processors
    """
    # Initialize empty lists and values
    cart_items = []
    total = 0
    product_count = 0
    # Get the cart from the session, or an empty dict if it doesn't exist
    # Source: https://docs.djangoproject.com/en/5.1/topics/http/sessions/
    cart = request.session.get('cart', {})

    # Loop through each item in the cart
    for item_id, quantity in cart.items():
        # Get the product details from the database
        product = get_object_or_404(Book, pk=item_id)
        # Calculate the total price for all items
        total += quantity * product.price
        # Keep track of total number of items
        product_count += quantity
        # Add item details to the cart_items list
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'book': product,
        })

    # Apply free shipping for orders over $40
    if total >= 40:
        shipping = 0
    else:
        shipping = 5

    # Calculate the final total including shipping
    grand_total = total + Decimal(shipping)

    # Create context dictionary to be available in all templates
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'shipping': shipping,
        'grand_total': grand_total,
    }

    return context
