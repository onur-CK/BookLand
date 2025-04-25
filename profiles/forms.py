from django import forms
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from .models import UserProfile

class CustomSignupForm(SignupForm):
    """
    Custom signup form that extends the default allauth SignupForm.
    Currently doesn't add any additional fields, but can be extended in the future.
    """
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'date_of_birth')
        fields = ['default_phone_number', 'default_street_address',
                  'default_apartment', 'default_city',
                  'default_postal_code', 'default_country']
        
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address': 'Street Address',
            'default_apartment': 'Apartment, Suite, etc.',
            'default_city': 'City',
            'default_postal_code': 'Postal Code',
            'default_country': 'Country',
        }

        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]}*'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder    
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = "form-control"

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'