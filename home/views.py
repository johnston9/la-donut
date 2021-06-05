from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def shop(request):
    """ A view to return the shop page """

    return render(request, 'home/shop.html')
