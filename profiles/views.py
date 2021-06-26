from django.shortcuts import render


def profile(request):
    """ Render the profile.html page. """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
