# This file defines the data models for user profiles, wishlists, and testimonials
# Source: https://docs.djangoproject.com/en/5.1/topics/db/models/

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Book
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    # One-to-one relationship with Django's built-in User model
    # Source: https://docs.djangoproject.com/en/5.1/topics/db/examples/one_to_one/
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address = models.CharField(max_length=80, null=True, blank=True)
    default_apartment = models.CharField(max_length=80, null=True, blank=True)
    default_city = models.CharField(max_length=40, null=True, blank=True)
    default_postal_code = models.CharField(max_length=20, null=True, blank=True)
    default_country = models.CharField(max_length=40, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    Signal handler to automatically create/update profile when User is saved
    Source: https://docs.djangoproject.com/en/5.1/topics/signals/
    """
    if created:
        UserProfile.objects.create(user=instance)
    else: 
        #Existing users: just save the profile
        # This handles the case where a user might exist without a profile (can be created by admin)
        try:
            instance.userprofile.save()
        except User.userprofile.RelatedObjectDoesNotExist:
            # If the profile doesn't exist, create it
            UserProfile.objects.create(user=instance)

class WishlistItem(models.Model):
    """
    A model to store wishlist items for users
    """
    # ForeignKey creates a many-to-one relationship
    # Source: https://docs.djangoproject.com/en/5.1/topics/db/examples/many_to_one/
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensures a user can't add the same book to their wishlist multiple times
        # Source: https://docs.djangoproject.com/en/5.1/ref/models/options/#unique-together
        unique_together = ('user', 'book')
        ordering = ['-date_added']

    def __str__(self):
        return f"{self.user.username}'s wishlist item: {self.book.title}"
    

class Testimonial(models.Model):
    """
    Model for storing user testimonials
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='testimonials')
    title = models.CharField(max_length=100)
    content = models.TextField()
    # Add validators to ensure rating is between 1 and 5
    # Source: https://docs.djangoproject.com/en/5.1/ref/validators/
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating from 1 to 5 stars"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date_updated']
        verbose_name_plural = 'Testimonials'
    
    def __str__(self):
        return f"{self.user.username}'s testimonial: {self.title}"

