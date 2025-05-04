from django import template

register = template.Library()

@register.filter
def webp_image_url(image_url):
    """Convert image URL to WebP format"""
    if not image_url:
        return None
    
    # Split the URL and change extension to webp
    path_parts = image_url.rsplit('.', 1)
    webp_url = f"{path_parts[0]}.webp"
    
    return webp_url