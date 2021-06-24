"""All code taken from Code Institute's Boutique Ado
    project written by ckz8780."""

from django.http import HttpResponse


class StripeWH_Handler:
    """Function to handle all Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pay_intent_id = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        gift_wrapped = intent.metadata.gift_wrapped
        is_card = intent.metadata.is_card
        message = intent.metadata.message
        sliced = intent.metadata.sliced

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'charge111 Webhook received: {event["type"]}',
            status=200)

    def handle_charge_failed(self, event):
        """
        Handle the charge.failed webhook from Stripe
        """
        return HttpResponse(
            content=f'charge456 Webhook received: {event["type"]}',
            status=200)

    def handle_charge_succeeded(self, event):
        """
        Handle the charge.succeeded webhook from Stripe
        """
        return HttpResponse(
            content=f'charge444 Webhook received: {event["type"]}',
            status=200)
