from django.contrib import admin
from .models import UserProfile, WishlistItem

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'default_phone_number', 'default_city', 'default_country')
    search_fields = ('user__username', 'user__email', 'default_phone_number')
    list_filter = ('default_country',)

class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'date_added')
    search_fields = ('user__username', 'book__title')
    list_filter = ('date_added',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(WishlistItem, WishlistItemAdmin)