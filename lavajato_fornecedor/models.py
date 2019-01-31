# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class fornecedor(models.Model):
    LB = (
        ('1', 'Ok'),
        ('2', 'Restrito'),
    )
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=1, choices=LB, default=1)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=30, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    numero = models.CharField(max_length=200, null=True, blank=True)
    bairro = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    uf_cidade = models.CharField(max_length=2, null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome