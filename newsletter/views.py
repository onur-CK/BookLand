from django.shortcuts import render
from django.http import JsonResponse
from .forms import NewsletterForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            # Save the subscription
            form.save()
            
            # Get the email
            email = form.cleaned_data['email']
            
            # Send welcome email
            subject = "Welcome to BookLand's Newsletter!"
            html_message = render_to_string('newsletter/welcome.html', {'email': email})
            plain_message = f"Thank you for subscribing to BookLand's newsletter! We'll keep you updated with our latest books and offers."
            
            send_mail(
                subject,
                plain_message,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                html_message=html_message,
                fail_silently=False,
            )
            
            # Return success response
            return JsonResponse({
                'status': 'success', 
                'message': 'Thank you for subscribing to our newsletter. An email has been sent to {}'.format(email)
})
        else:
            # Return error response
            return JsonResponse({'status': 'error', 'message': 'This email address is already subscribed or invalid.'})
    
    # If not POST, return error
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})