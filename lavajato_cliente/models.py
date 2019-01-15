from django.db import models
from django.utils import timezone

# Create your models here.
class carro(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=200)
    placa = models.CharField(max_length=20, null=True, blank=True)
    cor = models.CharField(max_length=100, null=True, blank=True)
    observacao = models.CharField(max_length=300, null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome

class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    data_nasc = models.DateTimeField(null=True, blank=True)
    cpf = models.CharField(max_length=30, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    numero = models.CharField(max_length=200, null=True, blank=True)
    bairro = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    uf_cidade = models.CharField(max_length=2, null=True, blank=True)
    carros = models.ManyToManyField(carro)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome