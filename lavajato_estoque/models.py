from django.db import models
from django.utils import timezone

# Create your models here.
class produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_minima = models.DecimalField(max_digits=10, decimal_places=2)
    lucro = models.IntegerField(null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.str(id)

class lote(models.Model):
    id = models.AutoField(primary_key=True)
    prod = models.ForeignKey(produto,on_delete=models.CASCADE)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.str(id)

class retiradas(models.Model):
    OP = (
        ('1', 'Proprio'),
        ('2', 'Venda'),
    )
    id = models.AutoField(primary_key=True)
    uso = models.CharField(max_length=1, choices=OP)
    prod = models.ForeignKey(produto,on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.str(id)
