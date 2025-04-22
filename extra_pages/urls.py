from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us, name='contact_us'),
    path('faq/', views.faq, name='faq'),
    path('shipping_policy/', views.shipping_policy, name='shipping_policy'),
]