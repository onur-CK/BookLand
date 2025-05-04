from django import template

register = template.Library()

@register.filter
def webp_image_url(image_url, size='small'):
    """Convert image URL to WebP format with size options"""
    if not image_url:
        return None
    
    # Get the base filename without extension
    path_parts = image_url.rsplit('.', 1)
    base_path = path_parts[0]
    
    # Return the sized WebP version
    return f"{base_path}_{size}.webp"

@register.filter
def jpg_image_url(image_url, size='small'):
    """Fallback to JPG with size options"""
    if not image_url:
        return None
    
    # Get the base filename without extension
    path_parts = image_url.rsplit('.', 1)
    base_path = path_parts[0]
    
    # Return the sized JPG version
    return f"{base_path}_{size}.jpg"