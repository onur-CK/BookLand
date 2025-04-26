from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def subscribe(request):
    """Handle newsletter subscription"""
    if request.method == 'POST':
        email = request.POST.get('email', '')
        
        if email:
            # Send confirmation email
            subject = 'Welcome to BookLand Newsletter!'
            message = f'Thank you for subscribing to the BookLand newsletter with {email}. We\'re excited to share our latest book recommendations and special offers with you!'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]
            
            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,
            )
            
            messages.success(request, f'Thanks for subscribing! A confirmation email has been sent to {email}.')
        else:
            messages.error(request, 'Please enter a valid email address.')
    
    # Redirect back to the page they came from
    return redirect(request.META.get('HTTP_REFERER', 'home'))