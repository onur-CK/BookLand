from django.shortcuts import render
from django.http import JsonResponse
from .forms import NewsletterForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import logging

# Set up logging
logger = logging.getLogger(__name__)

def subscribe(request):
    """
    Handle newsletter subscription requests with improved error handling
    """
    if request.method == 'POST':
        try:
            # Initialize form with POST data
            form = NewsletterForm(request.POST)
            
            # Validate form data and save if valid
            if form.is_valid():
                # Save the subscription
                form.save()
                
                # Get the email
                email = form.cleaned_data['email']
                
                try:
                    # Send welcome email to the subscriber
                    subject = "Welcome to BookLand's Newsletter!"
                    # Use template for HTML email content
                    html_message = render_to_string('newsletter/welcome.html', {'email': email})
                    # Plain text fallback for email clients that don't support HTML
                    plain_message = f"Thank you for subscribing to BookLand's newsletter! We'll keep you updated with our latest books and offers."
                    
                    # Send the email with both HTML and plain text versions
                    send_mail(
                        subject,
                        plain_message,
                        settings.DEFAULT_FROM_EMAIL,  # From address from settings
                        [email],  # To address(es)
                        html_message=html_message,
                        fail_silently=True, 
                    )
                    
                    logger.info(f"Newsletter welcome email sent to {email}")
                except Exception as e:
                    # Log email sending error but don't fail the subscription
                    logger.error(f"Error sending newsletter welcome email: {str(e)}")
             
                # Return JSON success response for AJAX handling
                return JsonResponse({
                    'status': 'success', 
                    'message': 'Thank you for subscribing to our newsletter!'
                })
            else:
                # Check if it's a duplicate email error
                if 'email' in form.errors and 'unique' in str(form.errors['email']).lower():
                    return JsonResponse({
                        'status': 'error', 
                        'message': 'This email address is already subscribed.'
                    })
                else:
                    # Log detailed form errors
                    logger.error(f"Form validation error: {form.errors}")
                    return JsonResponse({
                        'status': 'error', 
                        'message': 'Please provide a valid email address.'
                    })
        except Exception as e:
            # Log any other exceptions
            logger.error(f"Unexpected error in newsletter subscription: {str(e)}")
            return JsonResponse({
                'status': 'error', 
                'message': 'An error occurred. Please try again later.'
            })
    
    # Handle non-POST requests with error response
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})