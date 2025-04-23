# Source: https://docs.djangoproject.com/en/5.1/topics/forms/
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    # Meta class defines the form's behavior and appearance
    class Meta:
        model = Order  # Form is based on the Order model
        # Only include these fields from the model
        fields = ('full_name', 'email', 'phone_number',
                  'street_address', 'apartment', 'city',
                  'postal_code', 'country',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        
        Source: https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/#overriding-the-default-fields
        """
        super().__init__(*args, **kwargs)
        # Define placeholder text for each field
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address': 'Street Address',
            'apartment': 'Apartment, Suite etc. (optional)',
            'city': 'City',
            'postal_code': 'Postal Code',
            'country': 'Country',
        }

        # Set autofocus on the first field (full_name)
        self.fields['full_name'].widget.attrs['autofocus'] = True
        
        # Loop through each field to apply custom styling
        for field in self.fields:
            # Add asterisk to required field placeholders
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