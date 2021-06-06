from django.shortcuts import render
from .models import Product

# Create your views here.


def products(request):
    """ A view to render the shop page when users use the search or nav links
        to browse products, which also includes a menu where users can
        filter or browse products from the page"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/shop.html', context)
