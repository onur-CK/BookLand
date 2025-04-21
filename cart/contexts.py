from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Book

def cart_contents(request):
    """
    Context processor to make cart contents available across all templates
    """
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Book, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'book': product,
        })

    shipping = 5
    grand_total = total + Decimal(shipping)

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'shipping': shipping,
        'grand_total': grand_total,
    }

    return context