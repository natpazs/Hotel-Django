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


class formCadastro(forms.Form):
    first_name = forms.CharField(label="Nome", max_length=20)
    last_name = forms.CharField(label="Sobrenome", max_length=20)
    user = forms.CharField(label="Usuário", max_length=20)
    email = forms.EmailField(label="Email", max_length=20)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

class formLogin(forms.Form):
    user = forms.CharField(label="Usuário", max_length=20)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)