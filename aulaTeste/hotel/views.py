from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .models import Hotel, Quarto, Usuario
from .forms import formNome, formCadastro, formLogin

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
                    <a href="http://127.0.0.1:8000/quarto">Voltar</a>
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

def cadastro(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel    
    dados_quarto = Quarto.objects.all()
    context["dados_quarto"] = dados_quarto

    if request.method == "POST":
        form = formCadastro(request.POST)
        if form.is_valid():

            var_first_name = form.cleaned_data['first_name']
            var_last_name = form.cleaned_data['last_name']
            var_user = form.cleaned_data['user']
            var_email = form.cleaned_data['email']
            var_password = form.cleaned_data['password']

            user = User.objects.create_user( username = var_user, email = var_email, password = var_password)
            user.first_name = var_first_name
            user.last_name = var_last_name
            user.save()

            return redirect('login')
    else:
        form = formCadastro()
        context['form'] = form
        return render(request, "cadastro.html", context)

def login(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel    
    dados_quarto = Quarto.objects.all()
    context["dados_quarto"] = dados_quarto

    if request.method == "POST":
        form = formLogin(request.POST)
        if form.is_valid():
            var_user = form.cleaned_data['user']
            var_password = form.cleaned_data['password']

            user = authenticate(username=var_user, password=var_password)
            if user is not None:
                return redirect('quarto')
            else:
                context['error'] = "Usuário ou senha incorretos"
    else:
        form = formLogin()

    context['form'] = form
    return render(request, "login.html", context)

def reserva(request):
    if not request.user.is_authenticated:
        form = formLogin()
        return render(request, 'login.html', {'form': form})