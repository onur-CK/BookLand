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

@register.filter
def webp_image_url(image_url):
    """Convert image URL to WebP format"""
    if not image_url:
        return None
    
    # Split the URL and change extension to webp
    path_parts = image_url.rsplit('.', 1)
    webp_url = f"{path_parts[0]}.webp"
    
    return webp_url

# Then update context processor
def categories_processor(request):
    """
    Context processor to add all categories to all templates
    """
    all_categories = Category.objects.all().order_by('name')

    context = {
        'all_categories': all_categories,
        'webp_image_url': webp_image_url,
    }

    return context