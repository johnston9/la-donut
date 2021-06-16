from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Size, Forsix


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    price = 0

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.web_price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'price': int(product.web_price)
            })

        elif 'items_with_size' in item_data.keys():
            product = get_object_or_404(Product, pk=item_id)
            sizes = get_object_or_404(Size, name=product.name)
            for size1, quantity in item_data['items_with_size'].items():
                sizeprice = size1
                print(sizeprice)
                print(size1)
                sizlist = [siz for siz in size1.split("_")]
                size = sizlist[0]
                price = int(float(sizlist[1]))
                total += quantity * price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'sizeprice': sizeprice,
                    'size': size,
                    'price': price,
                    'quantity': quantity,
                    'product': product,
                    'sizes': sizes,
                })
        
        elif 'items_with_forsix' in item_data.keys():
            product = get_object_or_404(Product, pk=item_id)
            forsixes = get_object_or_404(Forsix, name=product.name)
            for forsix1, quantity in item_data['items_with_forsix'].items():
                forsixprice = forsix1
                six = [six for six in forsix1.split("_")]
                forsix = six[0]
                price = int(float(six[1].strip()))
                total += quantity * price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'forsixprice': forsixprice,
                    'forsix': forsix,
                    'price': price,
                    'quantity': quantity,
                    'product': product,
                    'forsixes': forsixes
                })

    if total != 0 and total < settings.FREE_DELIVERY_TOTAL:
        delivery = 10
        free_delivery_gap = settings.FREE_DELIVERY_TOTAL - total
    else:
        delivery = 0
        free_delivery_gap = 0
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_gap': free_delivery_gap,
        'free_delivery_total': settings.FREE_DELIVERY_TOTAL,
        'grand_total': grand_total,
    }

    return context
