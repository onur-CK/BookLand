# Source: https://docs.djangoproject.com/en/5.1/ref/contrib/admin/
from django.contrib import admin
from django.contrib import admin
from .models import Order, OrderLineItem

# Inline admin class to display OrderLineItems within the Order admin view
# Source: https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#inlinemodeladmin-objects


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)  # Prevents editing calculated field

# Main Order admin configuration


class OrderAdmin(admin.ModelAdmin):
    # Include the inline items within the Order view
    inlines = (OrderLineItemAdminInline,)
    # Fields that cannot be edited
    readonly_fields = (
        'order_number', 'date', 'shipping_cost',
        'order_total', 'grand_total'
    )
    # Field organization in detail view
    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'street_address', 'apartment',
              'city', 'postal_code', 'country', 'shipping_cost',
              'order_total', 'grand_total',)
    # Columns displayed in the orders list
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'shipping_cost', 'grand_total',)
    # Default sorting by date, newest first
    ordering = ('-date',)

# Register models to make them accessible in the admin interface


admin.site.register(Order, OrderAdmin)
