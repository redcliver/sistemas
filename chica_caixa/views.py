from django.shortcuts import render
from .models import caixa_geral
from django.utils import timezone
import datetime
from decimal import *

# Create your views here.
def chica_caixa(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            date = timezone.now
            return render(request, 'chica_caixa/caixa_conferencia.html', {'title':'Conferir caixa', 'date':date})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def entrada(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            try:
                caixa = caixa_geral.objects.latest('id')
            except:
                caixa = caixa_geral(operacao=1, id_operacao=1, valor_operacao=0, descricao="Abertura", total=0)
                caixa.save()
            if request.method == 'POST' and request.POST.get('desc') != None:
                desc = request.POST.get('desc')
                valor = request.POST.get('valor')
                caixa = caixa_geral.objects.latest('id')
                ultimo_id = caixa.id_operacao
                ultimo_id = int(ultimo_id) + 1
                novo_total = caixa.total + Decimal(valor)
                nova_entrada = caixa_geral(operacao=1, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                nova_entrada.save()
                msg = "Entrada registrada com sucesso!"
                return render(request, 'chica_caixa/caixa_entrada.html', {'title':'Entrada', 'msg':msg})
            return render(request, 'chica_caixa/caixa_entrada.html', {'title':'Entrada'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def saida(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            if request.method == 'POST' and request.POST.get('desc') != None:
                desc = request.POST.get('desc')
                valor = request.POST.get('valor')
                caixa = caixa_geral.objects.latest('id')
                ultimo_id = caixa.id_operacao
                ultimo_id = int(ultimo_id) + 1
                novo_total = caixa.total - Decimal(valor)
                nova_saida = caixa_geral(operacao=2, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                nova_saida.save()
                msg = "Saida registrada com sucesso!"
                return render(request, 'chica_caixa/caixa_saida.html', {'title':'Saida', 'msg':msg})
            return render(request, 'chica_caixa/caixa_saida.html', {'title':'Saida'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def conferencia(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            hoje = datetime.date.today().strftime('%Y-%m-%d')
            caixas = caixa_geral.objects.filter(data__icontains=hoje)
            caixa = caixa_geral.objects.latest('id')
            total = caixa.total
            if request.method == 'POST' and request.POST.get('data') != None:
                hoje = request.POST.get('data')
                caixas = caixa_geral.objects.filter(data__icontains=hoje)
                return render(request, 'chica_caixa/caixa_conferencia.html', {'title':'Conferencia', 'caixas':caixas, 'hoje':hoje, 'total':total})
            return render(request, 'chica_caixa/caixa_conferencia.html', {'title':'Conferencia', 'caixas':caixas, 'hoje':hoje, 'total':total})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def fechar(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            if request.method == 'POST' and request.POST.get('valor') != None:
                desc = "Fechamento de caixa"
                valor = request.POST.get('valor')
                caixa = caixa_geral.objects.latest('id')
                ultimo_id = caixa.id_operacao
                ultimo_id = int(ultimo_id) + 1
                novo_total = caixa.total - Decimal(valor)
                nova_saida = caixa_geral(operacao=2, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                nova_saida.save()
                msg = "Caixa fechado com sucesso, retirada de R$ " + str(valor)
                return render(request, 'chica_caixa/caixa_fechar.html', {'title':'Fechar caixa', 'msg':msg})
            return render(request, 'chica_caixa/caixa_fechar.html', {'title':'Fechar caixa'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})