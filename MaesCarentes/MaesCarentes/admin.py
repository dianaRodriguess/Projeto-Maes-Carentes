from django.contrib import admin
from MaesCarentes.models import *
from django.contrib.auth.models import User
from django.contrib.auth import admin as auth_admin
from .forms import UserChangeForm, UserCreationForm

admin.site.register(Mae)
admin.site.register(Evento)

@admin.register(Usuarios)
class UsuarioAdmin(auth_admin.UserAdmin):
    form = UserChangeForm  
    add_form = UserCreationForm
    model = Usuarios
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ('Bairro', {'fields': ('bairro',)}),
        ('Rua', {'fields': ('rua',)}),
        ('Cidade', {'fields': ('cidade',)}),
        ('Telefone', {'fields': ('telefone',)}),
        ('CPF', {'fields': ('cpf',)}),
        ('CEP', {'fields': ('cep',)}),
    )
admin.site.register(DoacaoDinheiro)
admin.site.register(DoacaoItem)
admin.site.register(FormaPagamento)
admin.site.register(EstadoConservacao)
