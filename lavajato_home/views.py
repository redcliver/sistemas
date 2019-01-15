from django.shortcuts import render
from lavajato_contas.models import conta
from lavajato_estoque.models import produto
from lavajato_agenda.models import parcela
from lavajato_caixa.models import caixa_geral
from lavajato_controle.models import conta_empresa
from django.utils import timezone
import datetime

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = timezone.now().strftime('%Y-%m-%d')
            try:
                conta_geral = conta_empresa.objects.latest('id')
            except:
                conta_geral = conta_empresa(operacao=1, id_operacao=1, valor_operacao=0, descricao="Abertura", total=0)
                conta_geral.save()
            try:
                caixa = caixa_geral.objects.latest('id')
            except:
                caixa = caixa_geral(operacao=1, id_operacao=1, valor_operacao=0, descricao="Abertura", total=0)
                caixa.save()
            vencimento_conta = 0
            estoque_min = 0
            for c in conta.objects.filter(estado=1, data_venc__icontains=hoje).all():
                vencimento_conta = vencimento_conta + 1
            for p in produto.objects.all():
                if p.quantidade <= p.quantidade_minima or p.quantidade == p.quantidade_minima:
                    estoque_min = estoque_min + 1
            return render(request, 'lavajato_home/home.html', {'title':'Home', 'vencimento_conta':vencimento_conta, 'estoque_min':estoque_min})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def suporte(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            return render(request, 'lavajato_home/suporte.html', {'title':'Suporte'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})