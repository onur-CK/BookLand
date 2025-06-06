# This file defines the forms used in the profiles app
# Forms handle data validation and processing
# Source: https://docs.djangoproject.com/en/5.1/topics/forms/

from django import forms
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from .models import UserProfile
from .models import Testimonial
from django.core.exceptions import ValidationError


class CustomSignupForm(SignupForm):
    """
    Custom signup form that extends the default
    allauth SignupForm.
    Currently doesn't add any additional fields,
    but can be extended in the future.
    Source: https://django-allauth.readthedocs.io/en/latest/forms.html
    """
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user


class UserProfileForm(forms.ModelForm):
    # ModelForm provides a way to create a Form class from a Django model
    # Source: https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/
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
        Source: https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/#overriding-the-default-fields
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


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['title', 'content', 'rating']
        # Define custom widgets for form fields
        # Source: https://docs.djangoproject.com/en/5.1/ref/forms/widgets/
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'maxlength': 300,
                'placeholder': (
                    'Share your experience in 300 characters or less...'
                )
            }),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes to form fields
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title for your testimonial',
            'content': 'Share your experience in 300 characters or less...',
            'rating': 'Rate your experience (1-5)',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
            if field == 'content':
                self.fields[field].help_text = '300 characters maximum'
            if field == 'rating':
                self.fields[field].help_text = (
                    'Rate your experience from 1 to 5 stars'
                )
