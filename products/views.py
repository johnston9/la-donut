from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def shop(request):
    """ A view to render the shop page without the selector menu"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/shop.html', context)


def shop_menu(request):
    """ A view to render the shop page which includes a selector
        menu"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/shop_menu.html', context)


def view_item(request, product_id):
    """ A view to display each product's details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/view_item.html', context)
