from django.contrib import admin
from .models import NewsletterSubscriber

# Custom admin configuration for the NewsletterSubscriber model
# Source: https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#modeladmin-objects


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    # Customize which fields appear in the list display
    # Source: https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
    list_display = ('email', 'date_added', 'is_active')
    # Add filters in the right sidebar of the admin list page
    # Source: https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter
    list_filter = ('is_active', 'date_added')
    # Enable search functionality for specific fields
    # Source: https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields
    search_fields = ('email',)
    # Add a date-based navigation hierarchy for filtering
    # Source: https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.date_hierarchy
    date_hierarchy = 'date_added'
