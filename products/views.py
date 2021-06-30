"""Product App views
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Size, Forsix
from .forms import ProductForm, SizeForm, ForsixForm


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
    back_to_cats = None

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
        'forsixes': forsixes,
        'back_to_cats': back_to_cats
    }

    return render(request, 'products/view_item.html', context)


def add_product(request):
    """ Add a product to the shop """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        item_name = request.POST['name']
        print(item_name)
        request.session['new_name'] = item_name
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'Failed to add product.\
                Please check that the form is valid.')
        if 'is_for_six' in request.POST:
            messages.success(request, 'Product added now add the box\
                quantity prices')
            return redirect('add_forsix')
        elif 'is_sizes' in request.POST:
            messages.success(request, 'Product added now add the size\
                prices')
            return redirect('add_sizes')
        else:
            messages.success(request, 'Product added successfully')
            return redirect(reverse('add_product'))

    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def add_size(request):
    """ Add size prices to a product """
    if request.method == 'POST':
        form = SizeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Size Prices Added Successfully.\
                Process complete')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add prices.\
                Please check that the form is valid.')
    else:
        # size = Size.objects.get(name=name)
        name = request.session.get('new_name')
        form = SizeForm()
        print(name)
    
    template = 'products/add_size.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def add_forsix(request):
    """ Add forsix prices to a product """
    if request.method == 'POST':
        form = ForsixForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Box Prices Added Successfully')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add prices.\
                Please check that the form is valid.')
    else:
        new_name = request.session.get('new_name')
        form = ForsixForm()
        print(new_name)
        # product = get_object_or_404(name=itemname)
    template = 'products/add_forsix.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
