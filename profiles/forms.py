from django import forms
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    """
    Custom signup form that extends the default allauth SignupForm.
    Currently doesn't add any additional fields, but can be extended in the future.
    """
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user
    