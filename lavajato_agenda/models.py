from django.db import models
from django.utils import timezone
from lavajato_cliente.models import cliente, carro
from lavajato_controle.models import funcionario, servico

# Create your models here.
class servico_item(models.Model):
    CA = (
        ('1', 'Nao'),
        ('2', 'Sim'),
    )
    id = models.AutoField(primary_key=True)
    cancelado = models.CharField(max_length=1, choices=CA, default='1')
    func = models.ForeignKey(funcionario, on_delete=models.CASCADE)
    serv = models.ForeignKey(servico, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.__str__(id)

class pagamento(models.Model):
    TP = (
        ('1', 'Dinheiro'),
        ('2', 'Cartao Debito'),
        ('3', 'Cartao Credito'),
    )
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=1, choices=TP)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.__str__(id)

class parcela(models.Model):
    ESTADO = (
        ('1', 'Em Aberto'),
        ('2', 'Paga'),
    )
    id = models.AutoField(primary_key=True)
    numero_parcela = models.IntegerField(default=1)
    total_parcelas = models.IntegerField(default=1)
    estado = models.CharField(max_length=1, choices=ESTADO)
    pag = models.CharField(max_length=200, null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(default=timezone.now)
    data_pagamento = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.__str__(id)

class agenda(models.Model):
    ES = (
        ('1', 'Aberto'),
        ('2', 'Desmarcado'),
        ('3', 'Pago'),
    )
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=1, choices=ES)
    item_servico = models.ManyToManyField(servico_item)
    pag = models.ManyToManyField(pagamento)
    parcelas = models.ManyToManyField(parcela)
    total_parcelas = models.IntegerField(default=1)
    pagas_parcelas = models.IntegerField(default=0)
    cli = models.ForeignKey(cliente, on_delete=models.CASCADE)
    car = models.ForeignKey(carro, on_delete=models.CASCADE)
    data = models.DateTimeField(null=True, blank=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    boleto_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    boleto = models.DateTimeField(null=True, blank=True)
    obs = models.CharField(max_length=1000, null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.__str__(id)
