# This file contains view functions for handling user profiles,
# account management, and related features
# Views are responsible for processing requests and returning responses
# Source: https://docs.djangoproject.com/en/5.1/topics/http/views/

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, WishlistItem, Testimonial
from .forms import UserProfileForm, UserForm, TestimonialForm
from products.models import Book
from django.contrib.auth import logout


@login_required
def profile(request):
    """ Display the user's profile. """
    # Fetch the user's profile or return 404 if not found
    # Source: https://docs.djangoproject.com/en/5.1/topics/http/shortcuts/#get-object-or-404
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        # Handle the profile form data
        profile_form = UserProfileForm(request.POST, instance=profile)

        # Handle the user form data (first_name, last_name)
        # Source: https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/
        user_form = UserForm(request.POST, instance=request.user)

        # Save both forms if valid
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()  # Save User model data (first_name, last_name)
            profile_form.save()  # Save UserProfile model data
            # Display success message using Django's messages framework
            # Source: https://docs.djangoproject.com/en/5.1/ref/contrib/messages/
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request,
                'Update failed. Please ensure all fields are valid.'
            )
    else:
        # For GET requests, instantiate the forms with current data
        profile_form = UserProfileForm(instance=profile)
        user_form = UserForm(instance=request.user)

    # Set a context variable to indicate we're on the profile page
    # This helps the toast template know not to show cart information
    on_profile_page = True

    # Using the app and template format explicitly
    # after theTemplate Path Resolution Bug
    # (check TESTING.md for more information)
    # Source: https://docs.djangoproject.com/en/5.1/topics/templates/#template-loading
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
def delete_account(request):
    """ Delete the user's account """
    # Only process account deletion on POST requests for security
    # Source: https://docs.djangoproject.com/en/5.1/topics/http/decorators/#django.views.decorators.http.require_POST
    if request.method == 'POST':
        user = request.user

        # Log the user out first
        # Source: https://docs.djangoproject.com/en/5.1/topics/auth/default/#how-to-log-a-user-out
        logout(request)
        # Then delete the user - Django will cascade delete related objects
        user.delete()
        messages.success(
            request,
            'Your account has been successfully deleted.'
        )
        return redirect('home')

    # If not POST, redirect to profile
    return redirect('profile')


@login_required
def order_history(request):
    """ Display the user's order history """
    # Fetch the user's profile
    profile = get_object_or_404(UserProfile, user=request.user)

    # Get all orders for this user, ordered by date (newest first)
    # Using the related_name 'orders' defined in the Order model's ForeignKey
    # Source: https://docs.djangoproject.com/en/5.1/topics/db/queries/#following-relationships-backward
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
    # Fetch all wishlist items for the current user
    # Source: https://docs.djangoproject.com/en/5.1/topics/db/queries/#retrieving-specific-objects-with-filters
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
    # get_or_create returns a tuple (object, created)
    # where created is a boolean
    # Source: https://docs.djangoproject.com/en/5.1/ref/models/querysets/#get-or-create
    wishlist_item, created = WishlistItem.objects.get_or_create(
        user=request.user,
        book=book
    )

    if created:
        messages.success(
            request,
            f'{book.title} has been added to your wishlist'
            )
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
    redirect_url = request.POST.get('redirect_url')

    try:
        wishlist_item = WishlistItem.objects.get(user=request.user, book=book)
        wishlist_item.delete()
        messages.success(
            request,
            f'{book.title} has been removed from your wishlist'
        )
    except WishlistItem.DoesNotExist:
        messages.error(request, f'{book.title} was not in your wishlist')

    # Redirection to page they came from
    if redirect_url:
        return redirect(redirect_url)

    # If no redirection URL, go to product detail page
    return redirect('product_detail', book_id)


@login_required
def testimonials(request):
    """ Display and manage user testimonials """
    # Get user testimonials
    testimonials = Testimonial.objects.filter(user=request.user)

    if request.method == 'POST':
        # Handle new testimonial submission
        # Source: https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/#the-save-method
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            messages.success(
                request,
                'Testimonial submitted successfully! '
                'It will be reviewed before being published.'
            )
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


@login_required
def edit_testimonial(request, testimonial_id):
    """ Edit a specific testimonial """
    # Get the testimonial object ensuring it belongs to the current user
    testimonial = get_object_or_404(
        Testimonial,
        pk=testimonial_id,
        user=request.user
    )

    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Testimonial updated successfully!')
            return redirect('testimonials')
    else:
        form = TestimonialForm(instance=testimonial)

    template = 'profiles/edit_testimonial.html'
    context = {
        'form': form,
        'testimonial': testimonial,
    }

    return render(request, template, context)


def delete_testimonial(request, testimonial_id):
    """ Delete a specific testimonial """
    # Get the testimonial ensuring it belongs to the current user
    testimonial = get_object_or_404(
        Testimonial,
        pk=testimonial_id,
        user=request.user
    )

    if request.method == 'POST':
        testimonial.delete()
        messages.success(request, 'Testimonial deleted successfully!')
        return redirect('testimonials')

    template = 'profiles/delete_testimonial.html'
    context = {
        'testimonial': testimonial,
    }

    return render(request, template, context)


def public_testimonials(request):
    """Display all approved testimonials to all users"""
    # Get all approved testimonials, ordered by date (newest first!)
    approved_testimonials = Testimonial.objects.filter(
        is_approved=True
    ).order_by('-date_created')

    template = 'profiles/public_testimonials.html'
    context = {
        'testimonials': approved_testimonials,
    }

    return render(request, template, context)
