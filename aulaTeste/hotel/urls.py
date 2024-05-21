from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('quarto', views.quarto,  name="quarto"),
    path('reserva', views.nome, name="reserva"),
    path('cadastro', views.cadastro, name="cadastro"),
    path('login', views.login, name="login"),
]