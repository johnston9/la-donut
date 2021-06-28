"""All code taken from Code Institute's Boutique Ado
    project written by ckz8780 and Stripe Docs"""

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import stripe
from checkout.webhook_handler import StripewhHandler


@require_POST
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe and match them to
       their related function in the StripeWH_Handler function
       from webhook_handler.py"""

    # Set stripe keys from settings
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e_r:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e_r:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e_r:
        return HttpResponse(content=e_r, status=400)

    # Create an instance of the StripewhHandler function
    handler = StripewhHandler(request)

    # Map webhook events to their related handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
        'charge.failed': handler.handle_charge_failed,
        'charge.succeeded': handler.handle_charge_succeeded,
    }

    # Get the webhook type from Stripe
    event_type = event['type']

    # If a handler exists for the event get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response
