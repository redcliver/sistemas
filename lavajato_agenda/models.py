from django.db import models
from django.utils import timezone
from lavajato_cliente.models import cliente
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

class agenda(models.Model):
    PG = (
        ('1', 'Dinheiro'),
        ('2', 'Cartao Debito'),
        ('3', 'Cartao Credito'),
        ('4', 'Aberto'),
        ('5', 'Desmarcado'),
    )
    id = models.AutoField(primary_key=True)
    pagamento = models.CharField(max_length=1, choices=PG)
    item_servico = models.ManyToManyField(servico_item)
    cli = models.ForeignKey(cliente, on_delete=models.CASCADE)
    data = models.DateTimeField(null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.__str__(id)
