from django.db import models

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
    default_country = models.Charfield(max_length=40, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    
