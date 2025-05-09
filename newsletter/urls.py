from django.urls import path
from . import views

# URL configuration for newsletter app
urlpatterns = [
    # URL pattern for newsletter subscription endpoint
    # The 'name' parameter allows this URL to be referenced in
    # templates with {% url 'newsletter_subscribe' %}
    # Source: https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#url
    path('subscribe/', views.subscribe, name='newsletter_subscribe'),
]
