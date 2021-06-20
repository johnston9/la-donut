from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "The Shopping Bag is empty...add some goodies")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J4TWyAaz5nOc1RDr6jDdno6FNAzzWZLpeuQZ17JJdfPHyGyq74omVAmu5kv1XUNKeJlEwoAdA5a0b3TmMLUW0wW00jfFvXKj7',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
