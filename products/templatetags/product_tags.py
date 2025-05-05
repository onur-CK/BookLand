from django import template

register = template.Library()

@register.filter
def webp_image_url(image_url):
    """
    Currently returns the original image URL.
    For WebP conversion, a more complex solution with S3 would be needed.
    """
    return image_url