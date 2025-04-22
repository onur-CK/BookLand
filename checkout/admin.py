from django.contrib import admin
from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date', 'shipping_cost',
                      'order_total', 'grand_total')
    
    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'street_address', 'apartment',
              'city', 'postal_code', 'country', 'shipping_cost',
              'order_total', 'grand_total',)
    
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'shipping_cost', 'grand_total',)
    
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)