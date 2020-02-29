from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home',
        'nbar': 'home',
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'title': 'About',
        'nbar': 'about'
    }
    return render(request, 'about.html', context)
