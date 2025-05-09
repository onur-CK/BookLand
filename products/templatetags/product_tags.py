from django import template

register = template.Library()


@register.filter
def webp_image_url(image_url):
    """
    Returns the original image URL.
    For WebP conversion, a more complex solution with S3 will be
    implemented for beter lighthouse performance results.
    """
    return image_url
