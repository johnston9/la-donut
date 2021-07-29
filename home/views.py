from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def delivery(request):
    """ A view to return the delivery page """

    return render(request, 'home/delivery.html')


def resize(request):
    """ A view to return the resize image instructions page """

    return render(request, 'home/resize.html')
