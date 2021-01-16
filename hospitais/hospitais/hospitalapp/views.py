from django.shortcuts import render
from django.http import HttpResponse
from .forms import Hospitalform
from .models import Hospitais

# Create your views here.

def index(request):
    #return HttpResponse('<h1> Aqui é o index </h1>')
    return render(request, 'hospitais/index.html')

def hospital(request):
    #return HttpResponse('<h1> Aqui é a area de hospital </h1>')
    hospitais = Hospitais.objects.all()
    return render(request, 'hospitais/hospitais.html', {'hospitais': hospitais})

def criar_hospitais(request):
    form = Hospitalform(request.POST)
    if request.method == 'POST':
        form = Hospitalform(request.POST, request.FILES)
        if form.is_valid():
            hosp = form.save()
            hosp.save()
            form = Hospitalform()
    return render(request, 'hospitais/criar_hospitais.html', {'form': form})