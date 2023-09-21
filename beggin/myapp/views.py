from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Stewardesses, News

def home(request):
    return render(request, 'home.html')

def main(request):
    artykuly = News.objects.all()[:3]
    print(artykuly)

    return render(request, 'main.html', {'artykuly':artykuly})

def search_results(request):
    if 'nr_ewidencyjny' in request.GET:
        nr_ewidencyjny = request.GET['nr_ewidencyjny']
        results = Stewardesses.objects.filter(nr_ewidencyjny__icontains=nr_ewidencyjny)
    else:
        results = []

    return render(request, 'home.html', {'results': results})

def login(request):
    return render(request, 'login.html')