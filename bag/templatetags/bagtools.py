"""filter to calculate subtotal
"""
from django import template


register = template.Library()


@register.filter(name='sum_subtotal')
def sum_subtotal(price, quantity):
    """filter to calculate subtotal
    """
    return price * quantity
