from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, WishlistItem
from .forms import UserProfileForm
from products.models import Book

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    # Using the app and template format explicitly after the Template Path Resolution Bug(explained in TESTING.md)
    return render(
        request,
        'profiles/profile.html',  # Explicit path format
        {
            'form': form,
            'profile': profile,
            'year_range': range(1940, 2006), # Context variable
        }
    )

@login_required
def order_history(request):
    """ Display the user's order history """
    profile = get_object_or_404(UserProfile, user=request.user)
    
    # Get all orders for this user, ordered by date (newest first)
    orders = profile.orders.all().order_by('-date')

    template = 'profiles/order_history.html'
    context = {
        'profile': profile,
        'orders': orders,  # Pass orders to the template
    }

    return render(request, template, context)

@login_required
def wishlist(request):
    """ Display the user's wishlist """
    wishlist_items = WishlistItem.objects.filter(user=request.user)

    template = 'profiles/wishlist.html'
    context = {
        'wishlist_items': wishlist_items,
    }

    return render(request, template, context)

@login_required
def add_to_wishlist(request, book_id):
    """ Add a book to the user's wishlist """
    book = get_object_or_404(Book, pk=book_id)

    # Check if the item is already in the wishlist
    wishlist_item, created = WishlistItem.objects.get_or_create(
        user=request.user,
        book=book
    )

    if created:
        messages.success(request, f'{book.title} has been added to your wishlist')
    else:
        messages.info(request, f'{book.title} is already in your wishlist')

    # Redirection to page they came from
    redirect_url = request.POST.get('redirect_url')
    if redirect_url:
        return redirect(redirect_url)

    # If no redirection URL, go to product detail page
    return redirect('product_detail', book_id)

@login_required
def remove_from_wishlist(request, book_id):
    """ Remove a book from the user's wishlist """
    book = get_object_or_404(Book, pk=book_id)

    try:
        wishlist_item = WishlistItem.objects.get(user=request.user, book=book)
        wishlist_item.delete()
        messages.success(request, f'{book.title} has been removed from your wishlist')
    except WishlistItem.DoesNotExist:
        messages.error(request, f'{book.title} was not in your wishlist')

    # Redirection to wishlist page
    return redirect('wishlist')



