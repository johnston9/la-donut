"""Create the Order form
"""
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """Create the Order form
    """
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'county', 'postcode',
                  'country', 'message')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove labels
        and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'postcode': 'Post Code',
            'town_or_city': 'Town or City',
            'county': 'County, State or Area',
            'message': 'Message'
        }

        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'order-input-style'
            self.fields[field].label = False
