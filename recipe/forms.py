"""Forms for the Recipe model
"""
from django import forms
from .widgets import CustomClearableFileInput
from .models import Recipe, Comment


class RecipeForm(forms.ModelForm):
    """Form for the Recipe model
    """

    class Meta:
        model = Recipe
        fields = ('title', 'description', 'image', 'is_vegan',
                  'ingredients', 'preparation')

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['ingredients'].label = 'Please add each ingredient\
            to a new line'


class CommentForm(forms.ModelForm):
    """Form for the Recipe model
    """

    class Meta:
        model = Comment
        fields = ('name', 'recipe', 'comment', 'recipe')
