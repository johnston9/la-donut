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

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(item_id, quantity)
    #  print(request.session['bag'])
    return redirect(redirect_url)
