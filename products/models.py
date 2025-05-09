from django.db import models
# Source: https://docs.djangoproject.com/en/5.1/ref/validators/
# Using built-in validators to enforce value constraints
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image


class Category(models.Model):
    # Source: https://docs.djangoproject.com/en/5.1/ref/models/fields/#django.db.models.CharField
    # Using CharField for text fields with defined max lengths
    name = models.CharField(max_length=100, unique=True)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    # Source: https://docs.djangoproject.com/en/5.1/ref/models/options/
    # Setting more human-readable verbose name in Admin using Meta class
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name or self.name


class Book(models.Model):
    # Source: https://docs.djangoproject.com/en/5.1/ref/models/fields/#django.db.models.ForeignKey
    # Using ForeignKey to establish a many-to-one
    # relationship with Category
    category = models.ForeignKey(
        'Category', null=True, blank=True,
        on_delete=models.SET_NULL
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    # Source: https://docs.djangoproject.com/en/5.1/ref/models/fields/#django.db.models.DecimalField
    # Using DecimalField for currency values to avoid floating point precision issues
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    # Source: https://docs.djangoproject.com/en/5.1/ref/models/fields/#django.db.models.ImageField
    # Using ImageField for storing book cover images
    image = models.ImageField(null=True, blank=True)
    inventory = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    # Source: https://docs.djangoproject.com/en/5.1/ref/models/fields/#django.db.models.DateTimeField
    # Using auto_now_add and auto_now for automatic timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
