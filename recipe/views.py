"""Recipe App views
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm


def recipe(request):
    """ A view to return the recipe page """
    recipes = Recipe.objects.all()
    latest = Recipe.objects.last()
    context = {
        'recipes': recipes,
        'latest': latest
    }

    return render(request, 'recipe/recipe.html', context)


def add_recipe(request):
    """ A view to return the add recipe page """

    # redirect if user not superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, incorrect url')
        return redirect(reverse('shop'))

    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recipe Added Successfully.\
                Process complete')
            return redirect(reverse('shop'))
        else:
            messages.error(request, 'Failed to add Recipe.\
                Please check that the form is valid.')
    else:
        recipe_form = RecipeForm()
    context = {
        'form': recipe_form,
    }

    return render(request, 'recipe/add_recipe.html', context)


def add_comment(request):
    """ A view to return the recipe page """

    return render(request, 'recipe/add_comment.html')
