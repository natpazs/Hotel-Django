from django import forms

TIPOS_QUARTOS = (
    ("SOLTEIRO", "Solteiro"),
    ("CASAL","Casal"),
    ("CONFORTO","Conforto"),
    ("LUXO","Luxo")
)

class formNome(forms.Form):
    nome = forms.CharField(label="Nome:", max_length=20)
    email = forms.CharField(label="Email:", max_length=50)
    idade = forms.IntegerField(label="Idade:")
    endereco = forms.CharField(label="Endereço:", max_length=60)
    quarto = forms.ChoiceField(label="Quartos:", choices=TIPOS_QUARTOS)
    data = forms.DateTimeField(label="Data:", widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
