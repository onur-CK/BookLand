from django.db import models

# Newsletter subscriber model to store email subscriptions
# Source: https://docs.djangoproject.com/en/5.0/topics/db/models/


class NewsletterSubscriber(models.Model):
    # Email field with unique constraint to prevent duplicate subscriptions
    # Source: https://docs.djangoproject.com/en/5.0/ref/models/fields/#emailfield
    email = models.EmailField(unique=True)
    # Auto-populated timestamp field for tracking when user subscribed
    # Source: https://docs.djangoproject.com/en/5.0/ref/models/fields/#datetimefield
    date_added = models.DateTimeField(auto_now_add=True)
    # Boolean field to manage subscription status (active/inactive)
    # Source: https://docs.djangoproject.com/en/5.0/ref/models/fields/#booleanfield
    is_active = models.BooleanField(default=True)

    # String representation of the model for admin display
    # Source: https://docs.djangoproject.com/en/5.0/ref/models/instances/#str
    def __str__(self):
        return self.email
