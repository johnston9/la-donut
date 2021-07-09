"""Forms for the Product App
"""
from django import forms
from django.forms.widgets import HiddenInput
from .widgets import CustomClearableFileInput
from .models import Product, Category, Size, Forsix, Review


class ProductForm(forms.ModelForm):
    """Form for the Product model
    """

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names


class SizeForm(forms.ModelForm):
    """Form for the Size model for6for12for24
    """

    class Meta:
        model = Size
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget = forms.HiddenInput()
        self.fields['product'].widget = forms.HiddenInput()


class ForsixForm(forms.ModelForm):
    """Form for the Forsix model
    """

    class Meta:
        model = Forsix
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget = forms.HiddenInput()
        self.fields['product'].widget = forms.HiddenInput()


class ReviewForm(forms.ModelForm):
    """Form for the Review model
    """

    class Meta:
        model = Review
        fields = ('name', 'review', 'rating')
