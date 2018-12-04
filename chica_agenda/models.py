from django.db import models
from django.utils import timezone
from chica_cliente.models import cliente
from chica_controle.models import funcionario, servico

# Create your models here.
class agenda(models.Model):
    PG = (
        ('1', 'Dinheiro'),
        ('2', 'Cartao Debito'),
        ('3', 'Cartao Credito'),
        ('4', 'Aberto'),
    )
    id = models.AutoField(primary_key=True)
    pagamento = models.CharField(max_length=1, choices=PG)
    func = models.ForeignKey(funcionario, on_delete=models.CASCADE)
    serv = models.ForeignKey(servico, on_delete=models.CASCADE)
    cli = models.ForeignKey(cliente, on_delete=models.CASCADE)
    data = models.DateTimeField(null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.__str__(id)