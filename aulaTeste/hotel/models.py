from django.db import models
from django.utils import timezone

# Create your models here.

TIPOS_QUARTOS = (
    ("SOLTEIRO", "Solteiro"),
    ("CASAL","Casal"),
    ("CONFORTO","Conforto"),
    ("LUXO","Luxo")
)

class Hotel(models.Model):
    titulo = models.CharField(max_length = 50)
    descricao = models.TextField(max_length = 500)
    logo = models.ImageField(upload_to="logo/")

    def __str__(self):
        return self.titulo

class Quarto(models.Model):
    tipo = models.CharField(max_length=15,choices=TIPOS_QUARTOS)
    disponibilidade = models.IntegerField()
    valor = models.FloatField(max_length = 4)
    descricao = models.TextField(max_length = 255)
    foto_quarto = models.ImageField(upload_to="Foto_quarto")

    def __str__(self):
        return self.tipo
    
class Usuario(models.Model):
    nome= models.CharField(max_length=20)
    email= models.CharField(max_length=50)
    idade = models.IntegerField()
    endereco = models.CharField(max_length=60)
    quarto = models.CharField(max_length=15,choices=TIPOS_QUARTOS)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome