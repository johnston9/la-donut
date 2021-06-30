"""Views for the Profile App
"""
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Render the profile.html page. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your address has been\
                changed successfully')
        else:
            messages.error(request, 'Update unsuccessful.\
                 Please check the form is valid.')

    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'profile_update': True
    }

    return render(request, template, context)


def past_orders(request, order_number):
    """ Render the checkout_complete.html page for past order """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
    ))

    template = 'checkout/checkout_complete.html'
    context = {
        'order': order,
        'from_profile_page': True,
    }

    return render(request, template, context)
