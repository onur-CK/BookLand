from django.contrib import admin
from .models import Category, Book
from .views import optimize_image

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')
    search_fields = ('name', 'friendly_name')
    prepopulated_fields = {'name': ('friendly_name',)}

    def get_book_count(self, obj):
        return obj.book_set.count()
    
    get_book_count.short_description = 'Books'

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'price', 'rating', 'available', 'inventory')
    list_filter = ('category', 'available')
    search_fields = ('title', 'author', 'description')
    ordering = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('price', 'available', 'inventory')

    # Add fieldsets to organize the admin form better
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
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.all().order_by('friendly_name')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)



def save_model(self, request, obj, form, change):
    if form.cleaned_data.get('image'):
        obj.image = optimize_image(form.cleaned_data['image'])
    super().save_model(request, obj, form, change)