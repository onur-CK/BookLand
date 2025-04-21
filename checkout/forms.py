from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address', 'apartment', 'city',
                  'postal_code', 'country',)

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
            'country': 'Country',
        }

        