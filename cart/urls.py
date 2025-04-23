from django.urls import path
from . import views

# URL patterns for the cart app
# Source: https://docs.djangoproject.com/en/5.1/topics/http/urls/
urlpatterns = [
    # Display the cart contents
    path('', views.view_cart, name='view_cart'),
    
    # Add an item to the cart (takes item_id parameter)
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    
    # Adjust the quantity of an item in the cart
    path('adjust/<item_id>/', views.adjust_cart, name='adjust_cart'),
    
    # Remove an item completely from the cart
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),
]