from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Size, Forsix

# Create your views here.


def shop(request):
    """ A view to render the shop page without the selector menu"""

    products = Product.objects.all()
    sizes = Size.objects.all()
    forsixs = Forsix.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sort = request.GET['sort']
            if sort == 'category':
                sort = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort = f'-{sort}'
            products = products.order_by(sort)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search words")
                return redirect(reverse('shop'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)       

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'forsixs': forsixs,
        'sizes': sizes,
        'search_words': query,
        'categories_selected': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/shop.html', context)


def view_item(request, product_id):
    """ A view to display each product's details """

    sizes = None
    forsixes = None

    product = get_object_or_404(Product, pk=product_id)
    if product.is_sizes:
        sizes = get_object_or_404(Size, name=product.name)
    if product.is_for_six:
        forsixes = get_object_or_404(Forsix, name=product.name)

    if 'r' in request.GET:
        back_to_cats = request.GET['r']
        print(back_to_cats)

    context = {
        'product': product,
        'sizes': sizes,
        'forsixes': forsixes
    }

    return render(request, 'products/view_item.html', context)
