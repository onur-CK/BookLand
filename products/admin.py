from django.contrib import admin
from .models import Category, Book

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')
    search_fields = ('name', 'friendly_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'price', 'rating', 'available', 'inventory')
    list_filter = ('category', 'available')
    search_fields = ('title', 'author', 'description')
    ordering = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('price', 'available', 'inventory')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)