from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Size, Forsix


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.web_price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
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
