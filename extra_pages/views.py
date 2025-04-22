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