"""All code based on Code Institute's Boutique Ado
    project written by ckz8780, most is taken directly."""

from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product

import json
import time


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
        # gift_wrapped = intent.metadata.gift_wrapped
        # is_card = intent.metadata.is_card
        # message = intent.metadata.message
        # sliced = intent.metadata.sliced

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Change empty string value to None for shipping details in model
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
            
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
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
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
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created new order using webhook',
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
