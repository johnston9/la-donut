"""Configure admin for Orders
"""
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.StackedInline):
    """Set the OrderLineItem model inside the Order model
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """Configure the Order model
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'shopping_bag', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number',
              'street_address1', 'street_address2', 'county',
              'postcode', 'town_or_city', 'country', 'delivery_cost',
              'order_total', 'grand_total', 'gift_wrapped', 'is_card',
              'message', 'sliced', 'shopping_bag', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
