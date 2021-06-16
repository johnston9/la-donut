from django.shortcuts import render, redirect, reverse


def bag(request):
    """ A view that renders the bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add product to the shopping bag """

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
            else:
                bag[item_id]['items_with_size'][size] = quantity
        else:
            bag[item_id] = {'items_with_size': {size: quantity}}

    elif forsix:
        if item_id in list(bag.keys()):
            if forsix in bag[item_id]['items_with_forsix'].keys():
                bag[item_id]['items_with_forsix'][forsix] += quantity
            else:
                bag[item_id]['items_with_forsix'][forsix] = quantity
        else:
            bag[item_id] = {'items_with_forsix': {forsix: quantity}}
    
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """Update the quantity of a product to the new value"""

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

    if sizeprice:
        if quantity > 0:
            bag[item_id]['items_with_size'][sizeprice] = quantity
        else:
            del bag[item_id]['items_with_size'][sizeprice]
            if not bag[item_id]['items_with_size']:
                bag.pop(item_id)
    if forsixprice:
        if quantity > 0:
            bag[item_id]['items_with_forsix'][forsixprice] = quantity
        else:
            del bag[item_id]['items_with_forsix'][forsixprice]
            if not bag[item_id]['items_with_forsix']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('bag'))
