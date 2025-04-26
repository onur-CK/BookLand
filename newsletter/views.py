import json
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber

@require_POST
@csrf_exempt
def subscribe(request):
    data = json.loads(request.body)
    email = data.get('email')
    
    if not email:
        return JsonResponse({'error': 'Email is required'}, status=400)
    
    # Save to our database
    try:
        Subscriber.objects.create(email=email)
    except Exception:
        # Email already exists
        pass
    
    # Add to Mailchimp
    try:
        client = MailchimpMarketing.Client()
        client.set_config({
            "api_key": settings.MAILCHIMP_API_KEY,
            "server": settings.MAILCHIMP_DATA_CENTER
        })
        
        response = client.lists.add_list_member(settings.MAILCHIMP_EMAIL_LIST_ID, {
            "email_address": email,
            "status": "subscribed",
        })
        
        return JsonResponse({
            'success': True,
            'message': f'{email} has been successfully added to our mailing list!'
        })
    except ApiClientError as error:
        return JsonResponse({
            'success': False,
            'message': error.text
        }, status=400)