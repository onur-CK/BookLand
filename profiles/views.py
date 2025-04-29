from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, WishlistItem, Testimonial
from .forms import UserProfileForm, UserForm, TestimonialForm
from products.models import Book

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        # Handle the profile form data
        profile_form = UserProfileForm(request.POST, instance=profile)
        
        # Handle the user form data (first_name, last_name)
        user_form = UserForm(request.POST, instance=request.user)
        
        # Save both forms if valid
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()  # Save User model data (first_name, last_name)
            profile_form.save()  # Save UserProfile model data
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure all fields are valid.')
    else:
        # For GET requests, instantiate the forms with current data
        profile_form = UserProfileForm(instance=profile)
        user_form = UserForm(instance=request.user)

    # Set a context variable to indicate we're on the profile page
    # This helps the toast template know not to show cart information
    on_profile_page = True
    
    # Using the app and template format explicitly after the Template Path Resolution Bug
    return render(
        request,
        'profiles/profile.html',  # Explicit path format
        {
            'profile_form': profile_form,
            'user_form': user_form,
            'profile': profile,
            'on_profile_page': on_profile_page,  
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


@login_required
def testimonials(request):
    """ Display and manage user testimonials """
    # Get user testimonials
    testimonials = Testimonial.objects.filter(user=request.user)
    
    if request.method == 'POST':
        # Handle new testimonial submission
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            messages.success(request, 'Testimonial submitted successfully! It will be reviewed before being published.')
            return redirect('testimonials')
    else:
        # Display empty form for GET request
        form = TestimonialForm()
    
    template = 'profiles/testimonials.html'
    context = {
        'testimonials': testimonials,
        'form': form,
    }
    
    return render(request, template, context)
    