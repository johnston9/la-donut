"""All code based on Code Institute's Boutique Ado
    project written by ckz8780."""

import json
import stripe
from django.shortcuts import render, redirect, reverse, get_object_or_404, \
    HttpResponse
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

from bag.contexts import bag_contents
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from products.models import Product
from .forms import OrderForm
from .models import Order, OrderLineItem


@require_POST
def extra_checkout_info(request):
    """
    Function to add metadata to the payment intent
    """
    try:
        pay_intent_id = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pay_intent_id, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'gift_wrapped': request.POST.get('gift_wrapped'),
            'is_card': request.POST.get('is_card'),
            'message': request.POST.get('message'),
            'sliced': request.POST.get('sliced'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e_r:
        messages.error(request, 'Your card did not go through.\
            Please try again or contact us and we will sort it out.')
        return HttpResponse(content=e_r, status=400)


def checkout(request):
    """
    Function to handle all checkout stuff
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'postcode': request.POST['postcode'],
            'county': request.POST['county'],
            'country': request.POST['country'],
            'message': request.POST['message'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pay_intent_id = request.POST.get(
                'client_secret').split('_secret')[0]
            order.stripe_pid = pay_intent_id
            order.shopping_bag = json.dumps(bag)
            order.stripe_pid = pay_intent_id
            if 'is_card' in request.POST:
                order.is_card = True
            if 'gift_wrapped' in request.POST:
                order.gift_wrapped = True
            if 'sliced' in request.POST:
                order.sliced = True

            order.save()
            for item_id, item_data in bag.items():
                try:
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

                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the items in your bag is out of stock \
                            Please call us and we'll quickly find you an \
                                alternative")
                    )
                    order.delete()
                    return redirect(reverse('get_bag'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_complete', args=[order.order_number]))
        else:
            messages.error(request, 'Sorry but there was an error processing\
                your form. Please check that your information is correct.')

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "The Shopping Bag is empty...\
                add some goodies")
            return redirect(reverse('shop'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.primary_full_name,
                    'email': profile.user.email,
                    'phone_number': profile.primary_phone_number,
                    'street_address1': profile.primary_street_address1,
                    'street_address2': profile.primary_street_address2,
                    'town_or_city': profile.primary_town_or_city,
                    'postcode': profile.primary_postcode,
                    'county': profile.primary_county,
                    'country': profile.primary_country,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Please check that you set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_complete(request, order_number):
    """
    Display order success comfirmation on completed checkouts
    """
    save_info = request.session.get('save_info')
    print(save_info)
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Enter the user's profile on the order
        order.user_profile = profile
        order.save()

        # Save the user's info to their userProfile model
        if save_info:
            profile_data = {
                'primary_full_name': order.full_name,
                'primary_phone_number': order.phone_number,
                'primary_country': order.country,
                'primary_postcode': order.postcode,
                'primary_town_or_city': order.town_or_city,
                'primary_street_address1': order.street_address1,
                'primary_street_address2': order.street_address2,
                'primary_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order number - {order_number}. \
        Your order has been successfully processed!')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_complete.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
