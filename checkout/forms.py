# Source: https://docs.djangoproject.com/en/5.1/topics/forms/
# Django Countries docs: https://pypi.org/project/django-countries/
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address', 'apartment', 'city',
                  'postal_code', 'country',)
        # Custom widget for country field to use Bootstrap styling
        # Source: https://django-crispy-forms.readthedocs.io/en/latest/
        widgets = {
            'country': CountrySelectWidget(attrs={
                'class': 'form-select',
            }),
        }
        
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address': 'Street Address',
            'apartment': 'Apartment, Suite etc. (optional)',
            'city': 'City',
            'postal_code': 'Postal Code',
        }

        # Set autofocus on the first field
        self.fields['full_name'].widget.attrs['autofocus'] = True
        
        # Loop through other fields for styling
        for field in self.fields:
            if field != 'country':  # Skip country as it has custom widget
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # Set placeholder text
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # Add Bootstrap class for consistent styling
            self.fields[field].widget.attrs['class'] = 'form-control'
            # Remove auto-generated labels
            self.fields[field].label = False