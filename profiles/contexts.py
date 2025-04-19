from .models import WishlistItem

def wishlist_count(request):
    """
    Context processor to add wishlist count to all templates
    """
    wishlist_count = 0

    if request.user.is_authenticated:
        wishlist_count = WishlistItem.objects.filter(user=request.user).count()

    context = {
        'wishlist_count': wishlist_count,
    }

    return context