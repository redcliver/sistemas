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

class reg_ponto(models.Model):
    ES = (
        ('1', 'Aberto'),
        ('2', 'Confirmado'),
    )
    OP = (
        ('1', 'Entrada'),
        ('2', 'Saida'),
    )
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=1, choices=ES)
    operacao = models.CharField(max_length=1, choices=OP)
    funcionario = models.CharField(max_length=200)
    data_confirmacao = models.DateTimeField(null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.__str__(id)

class conta_empresa(models.Model):
    OP = (
        ('1', 'Entrada'),
        ('2', 'Saida'),
    )
    id = models.AutoField(primary_key=True)
    operacao = models.CharField(max_length=1, choices=OP)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=300)
    id_operacao = models.CharField(max_length=200)
    valor_operacao = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.str(id)

class taxa(models.Model):
    TP = (
        ('1', 'Credito a Vista'),
        ('2', 'Credito a Prazo'),
        ('3', 'Debito'),
        ('4', 'Debito Elo'),
        ('5', 'Credito Elo'),
        ('6', 'Boleto'),
    )
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=1, choices=TP)
    dias = models.CharField(max_length=2, default=1)
    juros = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.__str__(tipo)