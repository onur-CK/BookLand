from django import template

# Create a new instance of Django's Library to register custom template filters
register = template.Library()


@register.filter
def subtract(value, arg):
    """
    {{ 40|subtract:total }} returns 40 - total
    """
    return value - arg