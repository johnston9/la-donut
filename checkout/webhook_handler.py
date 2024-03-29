"""Code based on Code Institute's Boutique Ado
    project written by ckz8780, most is taken directly."""

import json
import time
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from products.models import Product
from profiles.models import UserProfile
from .models import Order, OrderLineItem


class StripewhHandler:
    """Function to handle all Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

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
        if intent.metadata.gift_wrapped == 'true':
            gift_wrapped = True
        else:
            gift_wrapped = False
        if intent.metadata.is_card == 'true':
            is_card = True
        else:
            is_card = False
        if intent.metadata.sliced == 'true':
            sliced = True
        else:
            sliced = False
        message = intent.metadata.message

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.primary_phone_number = shipping_details.phone
                profile.primary_country = shipping_details.address.country
                profile.primary_postcode = shipping_details.address.postal_code
                profile.primary_town_or_city = shipping_details.address.city
                profile.primary_street_address1 = shipping_details.address.line1
                profile.primary_street_address2 = shipping_details.address.line2
                profile.primary_county = shipping_details.address.state
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                            full_name__iexact=shipping_details.name,
                            email__iexact=billing_details.email,
                            phone_number__iexact=shipping_details.phone,
                            street_address1__iexact=shipping_details.address.line1,
                            street_address2__iexact=shipping_details.address.line2,
                            town_or_city__iexact=shipping_details.address.city,
                            postcode__iexact=shipping_details.address.postal_code,
                            county__iexact=shipping_details.address.state,
                            country__iexact=shipping_details.address.country,
                            grand_total=grand_total,
                            shopping_bag=bag,
                            stripe_pid=pay_intent_id,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: \
                    Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    county=shipping_details.address.state,
                    country=shipping_details.address.country,
                    shopping_bag=bag,
                    stripe_pid=pay_intent_id,
                    gift_wrapped=gift_wrapped,
                    is_card=is_card,
                    sliced=sliced,
                    message=message,
                )
                for item_id, item_data in json.loads(bag).items():
                    if isinstance(item_data, int):
                        product = get_object_or_404(Product, pk=item_id)
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                            price=int(product.web_price)
                        )
                        order_line_item.save()

                    elif 'items_with_size' in item_data.keys():
                        product = get_object_or_404(Product, pk=item_id)
                        for size1, quantity in item_data[
                                'items_with_size'].items():
                            sizlist = [siz for siz in size1.split("_")]
                            size = sizlist[0]
                            price1 = int(float(sizlist[1]))
                            price = round(price1, 2)
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                size=size,
                                price=price
                            )
                            order_line_item.save()

                    elif 'items_with_forsix' in item_data.keys():
                        product = get_object_or_404(Product, pk=item_id)
                        for forsix1, quantity in item_data[
                                'items_with_forsix'].items():
                            six = [six for six in forsix1.split("_")]
                            forsix = six[0]
                            price1 = int(float(six[1].strip()))
                            price = round(price1, 2)
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                forsix=forsix,
                                price=price
                            )
                            order_line_item.save()
            except Exception as e_r:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook \
                        received: {event["type"]} | ERROR: {e_r}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: \
                Created new order using webhook', status=200)

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
