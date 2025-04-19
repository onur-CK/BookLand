from .models import Category

def categories_processor(request):
    """
    Context processor to add all categories to all templates
    """
    all_categories = Category.objects.all().order_by('name')

    context = {
        'all_categories': all_categories,
    }

    return context