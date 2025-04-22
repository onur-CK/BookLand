from django.shortcuts import render, redirect
from django.contrib import messages

def contact_us(request):
    """Render the Contact Us page and handle form submission"""
    if request.method == 'POST':
        name = request.POST.get('name')
        
        # Set a session variable for the success message
        request.session['contact_form_submitted'] = True
        request.session['contact_name'] = name
        
        # Redirect back to the contact page to prevent form resubmission on refresh
        return redirect('contact_us')
    
    # Check if we need to display a success message
    contact_success = False
    contact_name = ''
    if request.session.get('contact_form_submitted'):
        contact_success = True
        contact_name = request.session.get('contact_name', '')
        # Clear the session variables
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