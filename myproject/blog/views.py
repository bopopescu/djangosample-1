import datetime

from django.shortcuts import render


# Create your views here.

# View for Index page
def index(request):
    today = datetime.datetime.now().date()
    return render(request, 'blog/index.html', {"today": today})


# View for musings page
def musings(request):
    today = datetime.datetime.now().date()
    return render(request, 'blog/musings.html', {"today": today})


# View for Town page
def town(request):
    today = datetime.datetime.now().date()
    return render(request, 'blog/town.html', {"today": today})


# View for Links page
def links(request):
    today = datetime.datetime.now().date()
    return render(request, 'blog/links.html', {"today": today})
