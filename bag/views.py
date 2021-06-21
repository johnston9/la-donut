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
    sizeprice = None
    forsixprice = None

    if 'product_size' in request.POST:
        sizeprice = request.POST['product_size']
        size_price1 = sizeprice
        sizlist = [siz for siz in size_price1.split("_")]
        size = sizlist[0]

    if 'product_forsix' in request.POST:
        forsixprice = request.POST['product_forsix']
        forsix_price1 = forsixprice
        forsixlist = [sip for sip in forsix_price1.split("_")]
        box = forsixlist[0]
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if sizeprice:
        if item_id in list(bag.keys()):
            if sizeprice in bag[item_id]['items_with_size'].keys():
                bag[item_id]['items_with_size'][sizeprice] += quantity
                messages.success(request, f'Updated {size} {product.name}\
                    quantity to {bag[item_id]["items_with_size"][sizeprice]}')
            else:
                bag[item_id]['items_with_size'][sizeprice] = quantity
                messages.success(request, f'Added {quantity} {size} {product.name}\
                    to the shopping bag')
        else:
            bag[item_id] = {'items_with_size': {sizeprice: quantity}}
            messages.success(request, f'Added  {size} {product.name}\
                to the shopping bag')

    elif forsixprice:
        if item_id in list(bag.keys()):
            if forsixprice in bag[item_id]['items_with_forsix'].keys():
                bag[item_id]['items_with_forsix'][forsixprice] += quantity
                messages.success(request, f'Updated {product.name} {box} box quantity\
                    to {bag[item_id]["items_with_forsix"][forsixprice]}')
            else:
                bag[item_id]['items_with_forsix'][forsixprice] = quantity
                messages.success(request, f'Added {quantity} {product.name} \
                    {box} box to the shopping bag')
        else:
            bag[item_id] = {'items_with_forsix': {forsixprice: quantity}}
            messages.success(request, f'Added {product.name} \
                {box} box to the shopping bag')

    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name}\
                 quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {quantity} {product.name}\
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
        size_price1 = sizeprice
        print(sizeprice)
        print(size_price1)
        sizlist = [siz for siz in size_price1.split("_")]
        size = sizlist[0]
        print(size)

    if 'product_forsix' in request.POST:
        forsixprice = request.POST['product_forsix']
        forsix_price1 = forsixprice
        print(forsixprice)
        print(forsix_price1)
        forsixlist = [sip for sip in forsix_price1.split("_")]
        box = forsixlist[0]
        print(box)
    bag = request.session.get('bag', {})

    if forsixprice:
        if quantity > 0:
            bag[item_id]['items_with_forsix'][forsixprice] = quantity
            messages.success(request, f'Updated the quantity for {product.name}\
                {box} box to {bag[item_id]["items_with_forsix"][forsixprice]}')
        else:
            del bag[item_id]['items_with_forsix'][forsixprice]
            if not bag[item_id]['items_with_forsix']:
                bag.pop(item_id)
            messages.success(request, f'Deleted {product.name} \
                    {box} box from the shopping bag')

    elif sizeprice:
        if quantity > 0:
            bag[item_id]['items_with_size'][sizeprice] = quantity
            messages.success(request, f'Updated the quantity for {size} {product.name}\
                    to {bag[item_id]["items_with_size"][sizeprice]}')
        else:
            del bag[item_id]['items_with_size'][sizeprice]
            if not bag[item_id]['items_with_size']:
                bag.pop(item_id)
            messages.success(request, f'Deleted {size} {product.name} \
                    from the shopping bag')

    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name}\
                 quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} \
                from the shopping bag')

    request.session['bag'] = bag
    return redirect(reverse('bag'))


def remove_from_bag_six(request, item_id, forsixprice):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        forsix_price1 = forsixprice
        print(forsixprice)
        print(forsix_price1)
        forsixlist = [sip for sip in forsix_price1.split("_")]
        box = forsixlist[0]
        print(box)

        del bag[item_id]['items_with_forsix'][forsixprice]
        if not bag[item_id]['items_with_forsix']:
            bag.pop(item_id)
        messages.success(request, f'Deleted {product.name} \
                        "{ box } box" from the shopping bag')

        request.session['bag'] = bag
        return redirect(reverse('bag'))

    except Exception as e:
        messages.error(request, f'Error deleting item, {e} Please try again')
        return redirect(reverse('bag'))


def remove_from_bag_sizes(request, item_id, sizeprice):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        size_price1 = sizeprice
        print(sizeprice)
        print(size_price1)
        sizlist = [siz for siz in size_price1.split("_")]
        size = sizlist[0]
        print(size)

        del bag[item_id]['items_with_size'][sizeprice]
        if not bag[item_id]['items_with_size']:
            bag.pop(item_id)
        messages.success(request, f'Deleted {size} {product.name} \
            from the shopping bag')

        request.session['bag'] = bag
        return redirect(reverse('bag'))

    except Exception as e:
        messages.error(request, f'Error removing item: {e} Please try again')
        return redirect(reverse('bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} \
            from the shopping bag')

        request.session['bag'] = bag
        return redirect(reverse('bag'))

    except Exception as e:
        messages.error(request, f'Error deleting item, {e} Please try again')
        return redirect(reverse('bag'))
