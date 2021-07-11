"""Product App views
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from profiles.models import UserProfile
from .models import Product, Category, Size, Forsix, Review
from .forms import ProductForm, SizeForm, ForsixForm, ReviewForm


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
            category_name = request.GET['category'].split(',')
            products = products.filter(category__name__in=category_name)
            categories = Category.objects.filter(name__in=category_name)

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


def cakes_menu(request):
    """ A view to render the shop page using the cakes and desserts \
        select menu"""

    products = Product.objects.all()
    sizes = Size.objects.all()
    forsixs = Forsix.objects.all()
    categories = None

    if request.GET:
        category_name = request.GET['cakes_deserts'].split(',')        
        products = products.filter(category__name__in=category_name)        
        categories = Category.objects.filter(name__in=category_name)
        # category_name = request.GET['cakes_deserts']
        # products = products.filter(category__name=category_name)
        # categories = Category.objects.filter(name=category_name)

    context = {
        'products': products,
        'forsixs': forsixs,
        'sizes': sizes,
        'categories_selected': categories,
    }

    return render(request, 'products/shop.html', context)


def buns_menu(request):
    """ A view to render the shop page using the Buns select menu"""

    products = Product.objects.all()
    sizes = Size.objects.all()
    forsixs = Forsix.objects.all()
    categories = None

    if request.GET:
        category_name = request.GET['buns']
        products = products.filter(category__name=category_name)
        categories = Category.objects.filter(name=category_name)

    context = {
        'products': products,
        'forsixs': forsixs,
        'sizes': sizes,
        'categories_selected': categories,
    }

    return render(request, 'products/shop.html', context)


def box_menu(request):
    """ A view to render the shop page using the buns select menu"""

    products = Product.objects.all()
    sizes = Size.objects.all()
    forsixs = Forsix.objects.all()
    categories = None

    if request.GET:
        category_name = request.GET['box']
        products = products.filter(category__name=category_name)
        categories = Category.objects.filter(name=category_name)

    context = {
        'products': products,
        'forsixs': forsixs,
        'sizes': sizes,
        'categories_selected': categories,
    }

    return render(request, 'products/shop.html', context)


def view_item(request, product_id):
    """ A view to display each product's details """

    sizes = None
    forsixes = None
    back_to_cats = None

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product).order_by('-date_posted')

    if product.is_sizes:
        try:
            sizes = Size.objects.get(name=product.name)
        except Size.DoesNotExist:
            messages.info(request, (
                "This item has only one size")
            )

    if product.is_for_six:
        try:
            forsixes = Forsix.objects.get(name=product.name)
        except Forsix.DoesNotExist:
            messages.info(request, (
                "This item has only one size")
            )

    if 'r' in request.GET:
        back_to_cats = request.GET['r']
        print(back_to_cats)

    context = {
        'product': product,
        'reviews': reviews,
        'sizes': sizes,
        'forsixes': forsixes,
        'back_to_cats': back_to_cats
    }

    return render(request, 'products/view_item.html', context)


@login_required
def add_product(request):
    """ Add a product to the shop """

    # redirect if user not superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, incorrect url')
        return redirect(reverse('shop'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            if product.is_for_six:
                messages.info(request, 'Product added now add the box\
                    quantity prices')
                # return redirect('cost_forsix', args=[newproduct.id])
                return redirect('cost_forsix', product_id=product.id)
            elif product.is_sizes:
                messages.info(request, 'Product added now add the size\
                    prices')
                # return redirect('price_size', args=[newproduct.id])
                return redirect('price_size', product_id=product.id)
            else:
                messages.info(request, 'Product added successfully')
                return redirect(reverse('view_item', args=[product.id]))
                # return redirect(reverse('add_product'))

        else:
            messages.error(request, 'Failed to add product.\
                Please check that the form is valid.')

    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        'profile_update': True
    }

    return render(request, template, context)


@login_required
def price_size(request, product_id):
    """ Add size prices to a product """

    # redirect if user not superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, incorrect url')
        return redirect(reverse('shop'))

    product = get_object_or_404(Product, pk=product_id)
    size = get_object_or_404(Size, product=product)
    if request.method == 'POST':
        form = SizeForm(request.POST, instance=size)
        if form.is_valid():
            form.save()
            messages.info(request, 'Size Prices Added Successfully.\
                Process complete')
            return redirect(reverse('view_item', args=[product.id]))
            # return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add prices.\
                Please check that the form is valid.')
    else:
        form = SizeForm(instance=size)
    template = 'products/price_size.html'
    context = {
        'form': form,
        'product_id': product_id,
        'product': product
    }

    return render(request, template, context)


@login_required
def cost_forsix(request, product_id):
    """ Add forsix prices to a product """

    # redirect if user not superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, incorrect url')
        return redirect(reverse('shop'))

    product = get_object_or_404(Product, pk=product_id)
    forsix = get_object_or_404(Forsix, product=product)
    if request.method == 'POST':
        form = ForsixForm(request.POST, instance=forsix)
        if form.is_valid():
            form.save()
            messages.info(request, 'Box Prices Added Successfully')
            return redirect(reverse('view_item', args=[product.id]))
            # return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add prices.\
                Please check that the form is valid.')
    else:
        form = ForsixForm(instance=forsix)

    template = 'products/cost_forsix.html'
    context = {
        'form': form,
        'product_id': product_id,
        'product': product
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product """

    # redirect if user not superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, incorrect url')
        return redirect(reverse('shop'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        form.fields['name'].disabled = True
        form.fields['is_for_six'].disabled = True
        form.fields['is_sizes'].disabled = True
        if form.is_valid():
            form.save()
            messages.info(request, 'Product updated successfully')
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


@login_required
def sizeprice_edit(request, product_id):
    """ Edit a product's size prices"""

    # redirect if user not superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, incorrect url')
        return redirect(reverse('shop'))

    product = get_object_or_404(Product, pk=product_id)
    try:
        sizeprice = Size.objects.get(name=product.name)
    except Size.DoesNotExist:
        messages.error(request, (
            "This option is currently unavailable.")
        )
        return redirect(reverse('shop'))

    if request.method == 'POST':
        form = SizeForm(request.POST, instance=sizeprice)
        form.fields['name'].disabled = True
        form.fields['product'].disabled = True
        if form.is_valid():
            form.save()
            messages.info(request, 'Product prices updated successfully')
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


@login_required
def forsixprice_edit(request, product_id):
    """ Edit a product's box quantity (forsix) prices """

    # redirect if user not superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, incorrect url')
        return redirect(reverse('shop'))

    product = get_object_or_404(Product, pk=product_id)
    try:
        forsixprice = Forsix.objects.get(name=product.name)
    except Forsix.DoesNotExist:
        messages.error(request, (
            "This option is currently unavailable.")
        )
        return redirect(reverse('shop'))

    if request.method == 'POST':
        form = ForsixForm(request.POST, instance=forsixprice)
        # form.fields['name'].disabled = True
        # form.fields['product'].disabled = True
        if form.is_valid():
            form.save()
            messages.info(request, 'Product prices updated successfully')
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


@login_required
def delete_product(request, product_id):
    """ Delete a product """

    # redirect if user not superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, incorrect url')
        return redirect(reverse('shop'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.info(request, 'Product deleted!')
    return redirect(reverse('shop'))


@login_required
def review(request, product_id):
    """ Review a product """

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        review_f = ReviewForm(request.POST)
        if review_f.is_valid():
            saved_review = review_f.save(commit=False)
            if request.user.is_authenticated:
                profile = UserProfile.objects.get(user=request.user)
            saved_review.product = product
            saved_review.user_profile = profile
            saved_review.save()
            messages.info(request, f'Review for {product.name}\
                added successfully')
            return redirect(reverse('view_item', args=[product.id]))
        else:
            messages.error(request, 'Failed to add review\
                 Please check that the form is valid.')
    else:
        form = ReviewForm()

    template = 'products/review.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
