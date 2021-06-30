"""Form for the Product model
"""
from django import forms
from .models import Product, Category, Size, Forsix


class ProductForm(forms.ModelForm):
    """Form for the Product model
    """

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names


class SizeForm(forms.ModelForm):
    """Form for the Size model
    """

    class Meta:
        model = Size
        fields = '__all__'


class ForsixForm(forms.ModelForm):
    """Form for the Forsix model
    """

    class Meta:
        model = Forsix
        fields = '__all__'
