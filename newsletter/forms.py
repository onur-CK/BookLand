from django import forms
from .models import NewsletterSubscriber

# ModelForm for handling newsletter subscriptions
# Source: https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']

    def __init__(self, *args, **kwargs):
        # Override initialization to customize form attributes
        # Source: https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#overriding-the-default-fields
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes and styling to the email field
        # Source: https://getbootstrap.com/docs/5.0/forms/form-control/
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your email',
            'id': 'newsletter-email'
        })
