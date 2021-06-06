from django.shortcuts import render
from .models import Product

# Create your views here.


def shop(request):
    """ A view to render the shop page when users use the search-bar,
        shop button or nav-links, displaying their choices."""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/shop.html', context)


def shop_menu(request):
    """ A view to render the shop page when users use the search-bar,
        shop button or nav link displaying their choices which also 
        includes a menu where users can filter or browse products from the page"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/shop_menu.html', context)
