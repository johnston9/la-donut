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
        if form.is_valid():
            product = form.save()
            print(product)
            if product.is_for_six:
            # if 'is_for_six' in request.POST:
                messages.success(request, 'Product added now add the box\
                    quantity prices')
                # return redirect('cost_forsix', args=[newproduct.id])
                return redirect('cost_forsix', product_id=product.id)
            # elif 'is_sizes' in request.POST:
            elif product.is_sizes:
                messages.success(request, 'Product added now add the size\
                    prices')
                # return redirect('price_size', args=[newproduct.id])
                return redirect('price_size', product_id=product.id)
            else:
                messages.success(request, 'Product added successfully')
                return redirect(reverse('add_product'))

        else:
            messages.error(request, 'Failed to add product.\
                Please check that the form is valid.')

    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def price_size(request, product_id):
    """ Add size prices to a product """
    if request.method == 'POST':
        form = SizeForm(request.POST)
        # form.fields['name'].disabled = True
        # form.fields['product'].disabled = True
        if form.is_valid():
            form.save()
            messages.success(request, 'Size Prices Added Successfully.\
                Process complete')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add prices.\
                Please check that the form is valid.')
    else:
        product = get_object_or_404(Product, pk=product_id)
        form = SizeForm(initial={'product': product, 'name': product.name})

    template = 'products/price_size.html'
    context = {
        'form': form,
        'product_id': product_id,
        'product': product
    }

    return render(request, template, context)


def cost_forsix(request, product_id):
    """ Add forsix prices to a product """
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        form = ForsixForm(request.POST)
        # form.fields['name'].disabled = True
        # form.fields['product'].disabled = True
        if form.is_valid():
            form.save()
            messages.success(request, 'Box Prices Added Successfully')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add prices.\
                Please check that the form is valid.')
    else:
        product = get_object_or_404(Product, pk=product_id)
        form = ForsixForm(initial={'product': product, 'name': product.name})

    template = 'products/cost_forsix.html'
    context = {
        'form': form,
        'product_id': product_id,
        'product': product
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ Edit a product """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        form.fields['name'].disabled = True
        form.fields['is_for_six'].disabled = True
        form.fields['is_sizes'].disabled = True
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect(reverse('view_item', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.\
                 Please check that the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def sizeprice_edit(request, product_id):
    """ Edit a product's size prices"""
    product = get_object_or_404(Product, pk=product_id)
    sizeprice = get_object_or_404(Size, name=product.name)
    if request.method == 'POST':
        form = SizeForm(request.POST, request.FILES, instance=sizeprice)
        form.fields['name'].disabled = True
        form.fields['product'].disabled = True
        if form.is_valid():
            form.save()
            messages.success(request, 'Product prices updated successfully')
            return redirect(reverse('view_item', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product prices.\
                 Please check that the form is valid.')
    else:
        form = SizeForm(instance=sizeprice)
        messages.info(request, f'Editing {product.name} prices')

    template = 'products/sizeprice_edit.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def forsixprice_edit(request, product_id):
    """ Edit a product's box quantity (forsix) prices """
    product = get_object_or_404(Product, pk=product_id)
    forsixprice = get_object_or_404(Forsix, name=product.name)
    if request.method == 'POST':
        form = ForsixForm(request.POST, request.FILES, instance=forsixprice)
        form.fields['name'].disabled = True
        form.fields['product'].disabled = True
        if form.is_valid():
            form.save()
            messages.success(request, 'Product prices updated successfully')
            return redirect(reverse('view_item', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product prices.\
                 Please check that the form is valid.')
    else:
        form = ForsixForm(instance=forsixprice)
        messages.info(request, f'Editing {product.name} prices')

    template = 'products/forsixprice_edit.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    """ Delete a product """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('shop'))
