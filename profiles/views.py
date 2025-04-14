from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

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

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, template, context)

@login_required
def order_history(request):
    """ Display the user's order history """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/order_history.html'
    context = {
        'profile',
    }

    return render(request, template, context)

@login_required
def wishlist(request):
    """ Display the user's wishlist """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/wishlist.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
