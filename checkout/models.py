# Source: https://docs.djangoproject.com/en/5.1/topics/db/models/
from django.db import models
from products.models import Book
from profiles.models import UserProfile
import uuid  # For generating unique order numbers
from django.db.models import Sum
from django_countries.fields import CountryField


class Order(models.Model):
    # Unique order identifier - not editable by users
    order_number = models.CharField(max_length=32, null=False, editable=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    # Optional link to user profile - can be null for non-logged-in users
    # Source: https://docs.djangoproject.com/en/5.1/ref/models/fields/#django.db.models.ForeignKey
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, 
                                    null=True, blank=True, related_name='orders')
    
    # Customer details
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    
    # Shipping address
    street_address = models.CharField(max_length=80, null=False, blank=False)
    apartment = models.CharField(max_length=80, null=True, blank=True)  # Optional field
    city = models.CharField(max_length=40, null=False, blank=False)
    postal_code = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    
    # Order timestamps
    date = models.DateTimeField(auto_now_add=True)  # Set when order is created
    
    # Financial details
    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=5)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    
    # Stripe payment intent ID
    # Source: https://stripe.com/docs/payments/payment-intents
    stripe_pid = models.CharField(max_length=254, null=True, blank=True, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        Source: https://docs.python.org/3/library/uuid.html
        """
        return uuid.uuid4().hex.upper()
    
    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for shipping costs.
        Source: https://docs.djangoproject.com/en/5.1/topics/db/aggregation/
        """
        # Calculate total from all line items or default to 0
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        # Add shipping cost to get grand total
        self.grand_total = self.order_total + self.shipping_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        Source: https://docs.djangoproject.com/en/5.1/topics/db/models/#overriding-model-methods
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
    
class OrderLineItem(models.Model):
    # Link to parent order with cascade delete (if order deleted, delete line items)
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    # Link to specific book
    book = models.ForeignKey(Book, null=False, blank=False, on_delete=models.CASCADE)
    # Quantity of books ordered
    quantity = models.IntegerField(null=False, blank=False, default=0)
    # Per-line price calculation (book price × quantity)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.book.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Book {self.book.title} on order {self.order.order_number}'