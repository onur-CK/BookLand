# Django's render and redirect functions for view handling
# Source: https://docs.djangoproject.com/en/5.1/topics/http/shortcuts/
from django.shortcuts import render, redirect
# Django's messages framework to display one-time notifications
# Source: https://docs.djangoproject.com/en/5.1/ref/contrib/messages/
from django.contrib import messages

def contact_us(request):
    """Render the Contact Us page and handle form submission"""
    # POST/Redirect/GET pattern to prevent form resubmission
    # Source: https://en.wikipedia.org/wiki/Post/Redirect/Get
    if request.method == 'POST':
        name = request.POST.get('name')
        
        # Using Django's session framework to store temporary data
        # Source: https://docs.djangoproject.com/en/5.1/topics/http/sessions/
        request.session['contact_form_submitted'] = True
        request.session['contact_name'] = name
        
        # Redirect after POST to prevent form resubmission on page refresh
        # Source: https://docs.djangoproject.com/en/5.1/topics/http/shortcuts/#redirect
        return redirect('contact_us')
    
    # Check if we need to display a success message
    contact_success = False
    contact_name = ''
    if request.session.get('contact_form_submitted'):
        contact_success = True
        contact_name = request.session.get('contact_name', '')
        # Clear session variables after use to prevent stale data
        # Source: https://docs.djangoproject.com/en/5.1/topics/http/sessions/#setting-test-cookies
        request.session.pop('contact_form_submitted', None)
        request.session.pop('contact_name', None)
    
    return render(request, 'extra_pages/contact_us.html', {
        'contact_success': contact_success,
        'contact_name': contact_name,
    })

def faq(request):
    """Render the Frequently Asked Questions page"""
    return render(request, 'extra_pages/faq.html')

def shipping_policy(request):
    """Render the Shipping Policy page"""
    return render(request, 'extra_pages/shipping_policy.html')

def returns(request):
    """Render the Returns and Exchanges page"""
    return render(request, 'extra_pages/returns.html')

def privacy_policy(request):
    """Render the Privacy Policy page"""
    return render(request, 'extra_pages/privacy_policy.html')

def about_us(request):
    """Render the About Us page"""
    return render(request, 'extra_pages/about_us.html')