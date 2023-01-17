from django.forms import ModelForm
from django import forms
from django.contrib.auth import forms
from MaesCarentes.models import *

class MaeForm(ModelForm):
    class Meta:
        model = Mae
        fields = ['nome', 'dtnsc', 'telefone', 'qtdfilhos', 'cpf',
         'fonterenda', 'situtrabalho', 'moradia', 'cidade', 'bairro', 'rua']

class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['descricao', 'produto', 'dinheiro', 'mae']

class ProdutoForm(ModelForm):
    class Meta:
        model = DoacaoItem
        fields = ['nome', 'quantidade', 'estado', 'confirmacao', 'doado']

class DinheiroForm(ModelForm):
    class Meta:
        model = DoacaoDinheiro
        fields = ['valor', 'forma', 'confirmacao', 'doado']

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Usuarios
        fields = ['bairro', 'rua', 'cidade', 'telefone', 'cpf', 'cep']

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Usuarios
        fields = ['bairro', 'rua', 'cidade', 'telefone', 'cpf', 'cep']    
