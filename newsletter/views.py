from django.shortcuts import render
from django.http import JsonResponse
from .forms import NewsletterForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

# View function to handle newsletter subscription requests
# Source: https://docs.djangoproject.com/en/5.0/topics/http/views/
def subscribe(request):
    # Process subscription form data on POST request
    if request.method == 'POST':
        # Initialize form with POST data
        # Source: https://docs.djangoproject.com/en/5.0/topics/forms/#processing-the-data-from-a-form
        form = NewsletterForm(request.POST)
        # Validate form data and save if valid
        # Source: https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#the-save-method
        if form.is_valid():
            # Save the subscription
            form.save()
            
            # Get the email
            email = form.cleaned_data['email']
            
            # Send welcome email to the subscriber
            # Using Django's email functionality
            # Source: https://docs.djangoproject.com/en/5.0/topics/email/
            subject = "Welcome to BookLand's Newsletter!"
            # Use template for HTML email content
            # Source: https://docs.djangoproject.com/en/5.0/topics/templates/
            html_message = render_to_string('newsletter/welcome.html', {'email': email})
            # Plain text fallback for email clients that don't support HTML
            plain_message = f"Thank you for subscribing to BookLand's newsletter! We'll keep you updated with our latest books and offers."
            
            # Send the email with both HTML and plain text versions
            # Source: https://docs.djangoproject.com/en/5.0/topics/email/#send-mail
            send_mail(
                subject,
                plain_message,
                settings.DEFAULT_FROM_EMAIL, # From address from settings
                [email], # To address(es)
                html_message=html_message,
                fail_silently=False,
            )
            
            # Return JSON success response for AJAX handling
            # Source: https://docs.djangoproject.com/en/5.0/ref/request-response/#jsonresponse-objects
            return JsonResponse({
                'status': 'success', 
                'message': 'Thank you for subscribing to our newsletter. An email has been sent to {}'.format(email)
})
        else:
            # Return error response for invalid form (e.g., duplicate email)
            return JsonResponse({'status': 'error', 'message': 'This email address is already subscribed or invalid.'})
    
   # Handle non-POST requests with error response
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})