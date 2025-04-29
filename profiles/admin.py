from django.contrib import admin
from .models import UserProfile, WishlistItem, Testimonial

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

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'rating', 'date_created', 'is_approved')
    list_filter = ('is_approved', 'rating', 'date_created')
    search_fields = ('user__username', 'title', 'content')
    list_editable = ('is_approved',)
    readonly_fields = ('date_created', 'date_updated')
    actions = ['approve_testimonials', 'unapprove_testimonials']
    
    def approve_testimonials(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, f"{queryset.count()} testimonials approved.")
    approve_testimonials.short_description = "Approve selected testimonials"
    
    def unapprove_testimonials(self, request, queryset):
        queryset.update(is_approved=False)
        self.message_user(request, f"{queryset.count()} testimonials unapproved.")
    unapprove_testimonials.short_description = "Unapprove selected testimonials"

admin.site.register(Testimonial, TestimonialAdmin)