# This file contains a context processor for the wishlist count
# Context processors make variables available to all templates
# Source: https://docs.djangoproject.com/en/5.1/ref/templates/api/#writing-your-own-context-processors

from .models import WishlistItem

def wishlist_count(request):
    """
    Context processor to add wishlist count to all templates
    """
    wishlist_count = 0

    # Only count wishlist items for authenticated users
    if request.user.is_authenticated:
        wishlist_count = WishlistItem.objects.filter(user=request.user).count()

    return {'wishlist_count': wishlist_count}