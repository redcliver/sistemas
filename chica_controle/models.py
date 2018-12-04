from django.db import models
from django.utils import timezone

# Create your models here.
class funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=210)
    data_nasc = models.DateTimeField(null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome

class servico(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=210, null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome