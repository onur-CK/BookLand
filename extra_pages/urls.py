from django.urls import path
from . import views

urlpatterns = [
    # Define URL mapping for Contact Us page as the app's index
    path('', views.contact_us, name='contact_us'),
    # FAQ page URL pattern
    path('faq/', views.faq, name='faq'),
    # Shipping policy page URL pattern
    path('shipping_policy/', views.shipping_policy, name='shipping_policy'),
    # Returns policy page URL pattern
    path('returns/', views.returns, name='returns'),
    # Privacy policy page URL pattern - GDPR compliance
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('about_us/', views.about_us, name='about_us'),
]