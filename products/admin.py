from django.contrib import admin
from .models import Category, Book


# Admin configuration for the Category model
class CategoryAdmin(admin.ModelAdmin):
    # Display these fields in the category list view
    list_display = ('name', 'friendly_name')
    # Enable search functionality on these fields
    search_fields = ('name', 'friendly_name')
    # Automatically populate the 'name' field based on 'friendly_name' input
    prepopulated_fields = {'name': ('friendly_name',)}

    # Custom method to count the number of books in each category
    def get_book_count(self, obj):
        return obj.book_set.count()
    # Set column name in admin list view
    get_book_count.short_description = 'Books'


# Admin configuration for the Book model
class BookAdmin(admin.ModelAdmin):
    # Fields displayed in the book list view in admin
    list_display = ('title', 'author', 'category', 'price', 'rating', 'available', 'inventory')
    # Filters for the right sidebar in the list view
    list_filter = ('category', 'available')
    # Fields that can be searched using the search bar
    search_fields = ('title', 'author', 'description')
    # Default ordering of the book list
    ordering = ('title',)
    # Fields that are read-only (not editable in the admin form)
    readonly_fields = ('created_at', 'updated_at')
    # Fields that can be edited directly from the list view
    list_editable = ('price', 'available', 'inventory')

    # Fieldsets for organizing the admin form better
    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'author', 'description', 'category')
        }),
        ('Image', {
            'fields': ('image',)
        }),
        ('Pricing & Inventory', {
            'fields': ('price', 'inventory', 'available', 'rating')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    # Filter the foreign key dropdown for category to only show active categories
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
         # If the field is category, sort categories alphabetically by friendly name
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.all().order_by('friendly_name')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

# Register the models with their custom admin configurations 
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)

