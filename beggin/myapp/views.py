from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Stewardesses

def home(request):
    return render(request, 'home.html')

def main(request):
    return render(request, 'main.html')

def search_results(request):
    if 'nr_ewidencyjny' in request.GET:
        nr_ewidencyjny = request.GET['nr_ewidencyjny']
        results = Stewardesses.objects.filter(nr_ewidencyjny__icontains=nr_ewidencyjny)
    else:
        results = []

    return render(request, 'home.html', {'results': results})