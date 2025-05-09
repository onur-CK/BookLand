# Source: https://docs.djangoproject.com/en/5.1/ref/templates/api/#writing-your-own-context-processors
# Creating a context processor to make
# categories available across all templates
from .models import Category


def webp_image_url(image_url):
    """Convert image URL to WebP format"""
    if not image_url:
        return None

    # Split the URL and change extension to webp
    path_parts = image_url.rsplit('.', 1)
    webp_url = f"{path_parts[0]}.webp"

    return webp_url


def categories_processor(request):
    """
    Context processor to add all categories to all templates
    """
    # Source: https://docs.djangoproject.com/en/5.1/ref/models/querysets/#order-by
    # Retrieving and ordering categories by name for consistent display
    all_categories = Category.objects.all().order_by('name')

    # Return the categories in a context dictionary
    context = {
        'all_categories': all_categories,
    }

    return context
