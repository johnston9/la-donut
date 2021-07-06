"""Recipe App views
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from profiles.models import UserProfile
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm


def recipe(request):
    """ A view to return the recipe page """

    if request.method == 'POST':
        # redirect user not authenticated
        if not request.user:
            messages.error(request, 'Sorry, incorrect url')
            return redirect(reverse('shop'))

        form_data = {
            'name': request.POST['name'],
            'comment': request.POST['comment']
            }

        comment_form = CommentForm(form_data)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            redirect_url = request.POST.get('redirect_url')
            recipe_id = request.POST.get('recipe_id')
            this_recipe = get_object_or_404(Recipe, pk=recipe_id)
            comment.recipe = this_recipe
            if 'is_shop' in request.POST:
                comment.is_shop = True
            if request.user.is_authenticated:
                profile = UserProfile.objects.get(user=request.user)
            comment.user_profile = profile
            comment.save()
            messages.success(request, 'Comment Added Successfully')
            return redirect(redirect_url)
        else:
            messages.error(request, 'Failed to Add Comment.\
                 Please check that the form is valid.')
    else:
        form_c = CommentForm()
        print(form_c)

    recipes = Recipe.objects.all()
    latest = Recipe.objects.last()
    comments = Comment.objects.all()
    print(comments)
    context = {
        'recipes': recipes,
        'comments': comments,
        'latest': latest,
        'form': form_c
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
