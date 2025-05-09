from django.contrib import admin
from .models import UserProfile, WishlistItem, Testimonial

# Admin configuration for UserProfile model


class UserProfileAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = (
        'user', 'default_phone_number',
        'default_city', 'default_country'
    )
    # Add search functionality on these fields
    search_fields = ('user__username', 'user__email', 'default_phone_number')
    # Filter options in the sidebar
    list_filter = ('default_country',)

# Admin configuration for WishlistItem model


class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'date_added')
    search_fields = ('user__username', 'book__title')
    list_filter = ('date_added',)

# Register UserProfile and WishlistItem models with custom admin configuration


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(WishlistItem, WishlistItemAdmin)

# Admin configuration for Testimonial model


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'rating', 'date_created', 'is_approved')
    list_filter = ('is_approved', 'rating', 'date_created')
    # Search bar fields
    search_fields = ('user__username', 'title', 'content')
    # Make 'is_approved' editable from the list view
    list_editable = ('is_approved',)
    # Make timestamps read-only
    readonly_fields = ('date_created', 'date_updated')
    # Custom actions for approval/unapproval
    actions = ['approve_testimonials', 'unapprove_testimonials']

    # Custom admin action to approve selected testimonials
    def approve_testimonials(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(
            request,
            f"{queryset.count()} testimonials approved."
        )
    approve_testimonials.short_description = "Approve selected testimonials"

    # Custom admin action to unapprove selected testimonials
    def unapprove_testimonials(self, request, queryset):
        queryset.update(is_approved=False)
        self.message_user(
            request,
            f"{queryset.count()} testimonials unapproved."
        )
    unapprove_testimonials.short_description = (
        "Unapprove selected testimonials"
    )
# Register the Testimonial model with its custom admin class


admin.site.register(Testimonial, TestimonialAdmin)
