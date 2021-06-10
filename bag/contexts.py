from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

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
