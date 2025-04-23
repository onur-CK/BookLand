# Source: https://docs.djangoproject.com/en/5.1/topics/signals/
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total when OrderLineItem is created or updated
    
    Parameters:
    - sender: The model class (OrderLineItem)
    - instance: The actual instance being saved
    - created: Boolean flag for new instances vs updates
    - **kwargs: Additional arguments
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total when OrderLineItem is deleted
    
    This ensures the order total is recalculated whenever
    a line item is removed from an order.
    """
    instance.order.update_total()