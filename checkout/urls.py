from django.urls import path
from . import views
from .webhooks import webhook

# URL patterns for the checkout app
# Source: https://docs.djangoproject.com/en/5.1/topics/http/urls/
urlpatterns = [
    # Main checkout page - handles form submission and payment processing
    path('', views.checkout, name='checkout'),
    
    # Success page after order is completed
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    
    # Cache checkout data endpoint - stores metadata in Stripe payment intent
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    
    # Stripe webhook endpoint - receives and processes webhook events from Stripe
    path('wh/', webhook, name='webhook'),

    path('order_detail/<order_number>', views.order_detail, name='order_detail'),
]