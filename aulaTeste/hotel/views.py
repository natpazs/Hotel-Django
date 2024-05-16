from django.shortcuts import render, HttpResponse
from .models import Hotel, Quarto, Usuario
from .forms import formNome

def homepage(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    return render(request, 'homepage.html', context)

def quarto(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel    
    dados_quarto = Quarto.objects.all()
    context["dados_quarto"] = dados_quarto
    return render(request, 'quarto.html', context)

def nome(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel    
    dados_quarto = Quarto.objects.all()
    context["dados_quarto"] = dados_quarto
    if request.method == "POST":
        form = formNome(request.POST)
        if form.is_valid():
            ver_nome = form.cleaned_data['nome']
            ver_email = form.cleaned_data['email']
            ver_idade = form.cleaned_data['idade']
            ver_endereco = form.cleaned_data['endereco']
            ver_quarto = form.cleaned_data['quarto']
            ver_data = form.cleaned_data['data']

            user = Usuario(nome = ver_nome, email = ver_email, idade = ver_idade, endereco = ver_endereco, quarto = ver_quarto, data = ver_data)
            user.save()

            resposta = """
            <html>
            <head>
            <title>Reserva Bem Sucedida</title>
            <style>
            .container {
                text-align: center;
                margin-top: 50px;
            }
            </style>
            </head>
            <body>
            <div class="container">
                <h1>Reserva Bem Sucedida</h1>
                <form action="/pagina-de-volta/" method="get">
                    <a href="http://127.0.0.1:8000/">Voltar</a>
                </form>
            </div>
            </body>
            </html>
            """
            return HttpResponse(resposta)

    else:
        form = formNome()
    context['form'] = form
    return render(request, "reserva.html", context)