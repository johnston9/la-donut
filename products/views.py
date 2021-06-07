from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.


def shop(request):
    """ A view to render the shop page without the selector menu"""

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't \
                    enter any search criteria!")
                return redirect(reverse('shop'))
         
            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_words': query,
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
