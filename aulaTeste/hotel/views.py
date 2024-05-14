from django.shortcuts import render
from .models import Hotel, Quarto

def homepage(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    print (dados_hotel)
    return render(request, 'homepage.html', context)

def quarto(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel    
    dados_quarto = Quarto.objects.all()
    context["dados_quarto"] = dados_quarto
    print (dados_quarto)
    return render(request, 'quarto.html', context)