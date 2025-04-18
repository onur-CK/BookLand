from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Book

class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')
        ordering = ['-date_added']

        def __str__(self):
            return f"{self.user.username}'s wishlist item: {self.book.title}"

