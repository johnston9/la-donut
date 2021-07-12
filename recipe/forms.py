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

        self.fields['ingredients'].label = 'Please add a comma\
            after each ingredient'


class CommentForm(forms.ModelForm):
    """Form for the Recipe model
    """

    class Meta:
        model = Comment
        fields = ('name', 'comment')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs.update(style='max-height: 5em')
        self.fields['name'].widget.attrs.update(style='max-width: 15em')
        self.fields['comment'].widget.attrs['placeholder'] = 'Comments or \
            Questions'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['comment'].label = False
        self.fields['name'].label = False
