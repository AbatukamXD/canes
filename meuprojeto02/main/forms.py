from django import forms
from .models import Contato, User, Curso


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'senha']

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome','email', 'senha']

class InscricaoForm(forms.Form):
    cursos = forms.ModelMultipleChoiceField(
        queryset=Curso.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )