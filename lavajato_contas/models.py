from django.db import models
from django.utils import timezone

# Create your models here.
class conta(models.Model):
    ESTADO = (
        ('1', 'Em Aberto'),
        ('2', 'Paga'),
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data_venc = models.DateTimeField(null=True, blank=True)
    data_pagamento = models.DateTimeField(null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=1, choices=ESTADO)
    
    def __str__(self):
        return self.nome