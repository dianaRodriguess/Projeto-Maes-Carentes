from asyncio.windows_events import NULL
from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return self.cargo

class Usuarios(AbstractUser):
    bairro = models.CharField(max_length=50, blank=True, null=True)
    rua = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True, unique=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    
    def __str__(self):
        return self.first_name

class FormaPagamento(models.Model):
    id = models.AutoField(primary_key=True)
    forma = models.CharField(max_length=30)

    def __str__(self):
        return self.forma 

class EstadoConservacao(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "EstadosConservacao"

    def __str__(self):
        return self.estado 

class DoacaoDinheiro(models.Model):
    id = models.AutoField(primary_key=True)
    valor = models.FloatField()
    data = models.DateTimeField(timezone.make_aware, auto_now_add=True)
    forma = models.ForeignKey(FormaPagamento, on_delete = models.PROTECT)
    apoiador_id = models.ForeignKey(User, on_delete = models.PROTECT)
    confirmacao = models.BooleanField(default=False)
    doado = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "DoacoesDinheiro"

    def __str__(self):
        return str(self.valor)

class DoacaoItem(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    data = models.DateTimeField(timezone.make_aware, auto_now_add=True)
    quantidade = models.IntegerField()
    estado = models.ForeignKey(EstadoConservacao, on_delete = models.PROTECT)
    apoiador_id = models.ForeignKey(User, on_delete = models.PROTECT)
    confirmacao = models.BooleanField(default=False)
    doado = models.BooleanField(default=False)
    

    class Meta:
        verbose_name_plural = "DoacoesItens"

    def __str__(self):
        return self.nome    

class Mae(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    dtnsc = models.DateField()
    telefone = models.CharField(max_length=15)
    qtdfilhos = models.IntegerField()
    cpf = models.CharField(max_length=14)
    fonterenda = models.TextField(blank=True)
    situtrabalho = models.TextField(blank=True)
    moradia = models.TextField(blank=True)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    rua = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateTimeField(timezone.make_aware, auto_now_add=True)
    descricao = models.TextField()
    produto = models.ForeignKey(DoacaoItem, on_delete = models.CASCADE, blank=True, null=True, limit_choices_to={'confirmacao': True, 'doado': False})
    dinheiro = models.ForeignKey(DoacaoDinheiro, on_delete = models.CASCADE, blank=True, null=True, limit_choices_to={'confirmacao': True, 'doado': False})
    mae = models.ForeignKey(Mae, on_delete = models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.mae.nome




    