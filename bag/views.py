from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product


def bag(request):
    """ A view that renders the bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity') or 1)
    size = None
    forsix = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']

    if 'product_forsix' in request.POST:
        forsix = request.POST['product_forsix']
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_with_size'].keys():
                bag[item_id]['items_with_size'][size] += quantity
                messages.success(request, f'Updated {product.name} \
                    quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_with_size'][size] = quantity
                messages.success(request, f'Added {product.name} \
                    to the shopping bag')
        else:
            bag[item_id] = {'items_with_size': {size: quantity}}
            messages.success(request, f'Added {product.name} \
                to the shopping bag')

    elif forsix:
        if item_id in list(bag.keys()):
            if forsix in bag[item_id]['items_with_forsix'].keys():
                bag[item_id]['items_with_forsix'][forsix] += quantity
                messages.success(request, f'Updated {product.name} \
                    quantity to {bag[item_id]["items_with_forsix"][forsix]}')
            else:
                bag[item_id]['items_with_forsix'][forsix] = quantity
                messages.success(request, f'Added {product.name} \
                    to the shopping bag')
        else:
            bag[item_id] = {'items_with_forsix': {forsix: quantity}}
            messages.success(request, f'Added {product.name} \
                to the shopping bag')
    
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name}\
                 quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name}\
                 to the shopping bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """Update the quantity of a product to the new value"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    sizeprice = None
    forsixprice = None
    if 'product_size' in request.POST:
        sizeprice = request.POST['product_size']
        print(sizeprice)
    if 'product_forsix' in request.POST:
        forsixprice = request.POST['product_forsix']
        print(forsixprice)
    bag = request.session.get('bag', {})

    if forsixprice:
        if quantity > 0:
            bag[item_id]['items_with_forsix'][forsixprice] = quantity
        else:
            del bag[item_id]['items_with_forsix'][forsixprice]
            if not bag[item_id]['items_with_forsix']:
                bag.pop(item_id)
    
    elif sizeprice:
        if quantity > 0:
            bag[item_id]['items_with_size'][sizeprice] = quantity
        else:
            del bag[item_id]['items_with_size'][sizeprice]
            if not bag[item_id]['items_with_size']:
                bag.pop(item_id)

    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('bag'))


def remove_from_bag_sizes(request, item_id, item_size):
    """Remove the item from the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})

    del bag[item_id]['items_with_size'][item_size]
    if not bag[item_id]['items_with_size']:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('bag'))


def remove_from_bag_six(request, item_id, item_forsix):
    """Remove the item from the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})

    del bag[item_id]['items_with_forsix'][item_forsix]
    if not bag[item_id]['items_with_forsix']:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})

    bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('bag'))
