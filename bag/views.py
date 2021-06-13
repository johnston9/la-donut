from django.shortcuts import render, redirect


def bag(request):
    """ A view that renders the bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    size = None
    forsix = None
    price = None
    if 'product_size' in request.POST:
        size = request.post['product_size'].split('_')[0]
        price = request.post['product_size'].split('_')[1]

    if 'product_forsix' in request.POST:
        forsix = request.post['product_forsix'].split('_')[0]
        price = request.post['product_forsix'].split('_')[1]
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_with_size'].keys():
                bag[item_id]['items_with_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_with_size"][size]}')
            else:
                bag[item_id]['items_with_size'][size] = quantity
                bag[item_id]['items_with_size'][size][quantity] = price
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            bag[item_id] = {'items_with_size': {size: {quantity: price}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')

    elif forsix:
        if item_id in list(bag.keys()):
            if forsix in bag[item_id]['items_with_forsix'].keys():
                bag[item_id]['items_with_forsix'][forsix] += quantity
                messages.success(request, f'Updated {forsix.upper()} {product.name} quantity to {bag[item_id]["items_with_forsix"][forsix]}')
            else:
                bag[item_id]['items_with_forsix'][forsix] = quantity
                bag[item_id]['items_with_size'][forsix][quantity] = price
                messages.success(request, f'Added {forsix.upper()} {product.name} to your bag')
        else:
            bag[item_id] = {'items_with_forsix': {forsix: {quantity: price}}
            messages.success(request, f'Added {forsix.upper()} {product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(item_id, quantity)
    #  print(request.session['bag'])
    return redirect(redirect_url)
