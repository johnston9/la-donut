"""Recipe App views
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import UserProfile
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm


def recipe(request):
    """ A view to return the recipes page """

    recipes = Recipe.objects.all()
    latest = Recipe.objects.last()
    context = {
        'recipes': recipes,
        'latest': latest,
    }

    return render(request, 'recipe/recipe.html', context)


def get_recipe(request, recipe_id):
    """ A view to return the recipe page """

    recipe_one = get_object_or_404(Recipe, pk=recipe_id)
    print(recipe_one)
    # list = recipe_one.ingedients.split(',')
    context = {
        'recipe': recipe_one,
        'ingredients': list,
    }

    return render(request, 'recipe/get_recipe.html', context)


def latest_recipe(request):
    """ A view to return the recipe page """

    last_recipe = Recipe.objects.last()
    context = {
        'recipe': last_recipe,
    }

    return render(request, 'recipe/get_recipe.html', context)


def add_recipe(request):
    """ A view to return the add recipe page """

    # redirect if user not superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, incorrect url')
        return redirect(reverse('shop'))

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Recipe Added Successfully.\
                Process complete')
            return redirect(reverse('recipe'))
        else:
            messages.error(request, 'Failed to add Recipe.\
                Please check that the form is valid.')
    else:
        recipe_form = RecipeForm()
    context = {
        'form': recipe_form,
    }

    return render(request, 'recipe/add_recipe.html', context)


def edit_recipe(request, recipe_id):
    """ A view to return the edit recipe page """

    # redirect if user not superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, incorrect url')
        return redirect(reverse('shop'))

    recipe1 = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe1)
        if form.is_valid():
            form.save()
            messages.info(request, 'Recipe Edited Successfully.\
                Process complete')
            return redirect(reverse('get_recipe', args=[recipe1.id]))
        else:
            messages.error(request, 'Failed to Edit Recipe.\
                Please check that the form is valid.')
    else:
        recipe_form = RecipeForm(instance=recipe1)
        messages.info(request, f'Editing {recipe1.title}')
    context = {
        'form': recipe_form,
        'recipe': recipe1
    }

    return render(request, 'recipe/edit_recipe.html', context)


def chat(request):
    """ A view to return the chat page """

    if request.method == 'POST':
        form_data = {
            'name': request.POST['name'],
            'comment': request.POST['comment']
            }

        comment_form = CommentForm(form_data)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            redirect_url = request.POST.get('redirect_url')
            if 'is_shop' in request.POST:
                comment.is_shop = True
            if request.user.is_authenticated:
                profile = UserProfile.objects.get(user=request.user)
            comment.user_profile = profile
            comment.save()
            messages.info(request, 'Comment Added Successfully')
            return redirect(redirect_url)
        else:
            messages.error(request, 'Failed to Add Comment.\
                 Please check that the form is valid.')
    else:
        form_c = CommentForm()

    comments = Comment.objects.order_by('-date_posted')
    context = {
        'comments': comments,
        'form': form_c
    }

    return render(request, 'recipe/chat.html', context)


@login_required
def delete_recipe(request, recipe_id):
    """ Delete a recipe """

    # redirect if user not superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, incorrect url')
        return redirect(reverse('shop'))

    recipe_del = get_object_or_404(Recipe, pk=recipe_id)
    recipe_del.delete()
    messages.info(request, 'Recipe deleted!')
    return redirect(reverse('recipe'))


@login_required
def cut_comment(request, comment_id):
    """ Delete a comment """

    # redirect if user not superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, incorrect url')
        return redirect(reverse('shop'))

    comment_del = get_object_or_404(Comment, pk=comment_id)
    comment_del.delete()
    messages.info(request, 'Comment deleted!')
    return redirect(reverse('chat'))
