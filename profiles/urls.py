from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/', views.order_history, name='order_history'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:book_id>', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<int:book_id>', views.remove_from_wishlist, name='remove_from_wishlist'),
]