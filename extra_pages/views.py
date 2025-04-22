from django.shortcuts import render

def contact_us(request):
    """Render the Contact Us page"""
    return render(request, 'extra_pages/contact_us.html')

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