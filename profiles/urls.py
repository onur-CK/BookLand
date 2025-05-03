from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/', views.order_history, name='order_history'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:book_id>', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<int:book_id>', views.remove_from_wishlist, name='remove_from_wishlist'),
    # Testimonial URLs
    path('testimonials/', views.testimonials, name='testimonials'),
    path('testimonials/edit/<int:testimonial_id>/', views.edit_testimonial, name='edit_testimonial'),
    path('testimonials/delete/<int:testimonial_id>/', views.delete_testimonial, name='delete_testimonial'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('public-testimonials/', views.public_testimonials, name='public_testimonials'),
]