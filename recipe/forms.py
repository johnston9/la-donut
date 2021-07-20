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
                  'prep_time', 'cook_time', 'serves',
                  'ingredient1', 'ingredient2', 'ingredient3',
                  'ingredient4', 'ingredient5', 'ingredient6',
                  'ingredient7', 'ingredient7', 'ingredient9',
                  'ingredient10', 'step1', 'step2', 'step3')

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['description'].widget.attrs.update(style='max-height: 5em')
        self.fields['step1'].widget.attrs.update(style='max-height: 5em')
        self.fields['step2'].widget.attrs.update(style='max-height: 5em')
        self.fields['step3'].widget.attrs.update(style='max-height: 5em')
        self.fields['prep_time'].label = 'Preparation Time, e.g. 30 Minutes'
        self.fields['cook_time'].label = 'Cooking Time, e.g. 30 Minutes'
        self.fields['serves'].label = 'Serves, e.g. 4 People'


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
        self.fields['comment'].widget.attrs['placeholder'] = 'Comments'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['comment'].label = False
        self.fields['name'].label = False
