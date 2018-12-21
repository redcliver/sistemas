from django.shortcuts import render
from .models import caixa_geral
from lavajato_agenda.models import agenda, servico_item
from lavajato_controle.models import funcionario, servico
from lavajato_contas.models import conta
from django.utils import timezone
import datetime
from decimal import *

# Create your views here.
def lavajato_caixa(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            date = timezone.now
            return render(request, 'lavajato_caixa/caixa_conferencia.html', {'title':'Conferir caixa', 'date':date})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def entrada(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
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
                desc = "Entrada - "+desc
                novo_total = caixa.total + Decimal(valor)
                nova_entrada = caixa_geral(operacao=1, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                nova_entrada.save()
                msg = "Entrada registrada com sucesso!"
                return render(request, 'lavajato_caixa/caixa_entrada.html', {'title':'Entrada', 'msg':msg})
            return render(request, 'lavajato_caixa/caixa_entrada.html', {'title':'Entrada'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def saida(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            if request.method == 'POST' and request.POST.get('desc') != None:
                desc = request.POST.get('desc')
                valor = request.POST.get('valor')
                caixa = caixa_geral.objects.latest('id')
                ultimo_id = caixa.id_operacao
                ultimo_id = int(ultimo_id) + 1
                desc = "Retirada - "+desc
                novo_total = caixa.total - Decimal(valor)
                nova_saida = caixa_geral(operacao=2, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                nova_saida.save()
                msg = "Saida registrada com sucesso!"
                return render(request, 'lavajato_caixa/caixa_saida.html', {'title':'Saida', 'msg':msg})
            return render(request, 'lavajato_caixa/caixa_saida.html', {'title':'Saida'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def conferencia(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = datetime.date.today().strftime('%Y-%m-%d')
            caixas = caixa_geral.objects.filter(data__icontains=hoje)
            caixa = caixa_geral.objects.latest('id')
            total = caixa.total
            if request.method == 'POST' and request.POST.get('data') != None:
                hoje = request.POST.get('data')
                caixas = caixa_geral.objects.filter(data__icontains=hoje)
                return render(request, 'lavajato_caixa/caixa_conferencia.html', {'title':'Conferencia', 'caixas':caixas, 'hoje':hoje, 'total':total})
            return render(request, 'lavajato_caixa/caixa_conferencia.html', {'title':'Conferencia', 'caixas':caixas, 'hoje':hoje, 'total':total})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def fechar(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            if request.method == 'POST' and request.POST.get('valor') != None:
                desc = "Retirada - Fechamento de caixa"
                valor = request.POST.get('valor')
                caixa = caixa_geral.objects.latest('id')
                ultimo_id = caixa.id_operacao
                ultimo_id = int(ultimo_id) + 1
                novo_total = caixa.total - Decimal(valor)
                nova_saida = caixa_geral(operacao=2, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                nova_saida.save()
                msg = "Caixa fechado com sucesso, retirada de R$ " + str(valor)
                return render(request, 'lavajato_caixa/caixa_fechar.html', {'title':'Fechar caixa', 'msg':msg})
            return render(request, 'lavajato_caixa/caixa_fechar.html', {'title':'Fechar caixa'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def balanco(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = datetime.date.today()
            hj = datetime.date.today().strftime('%Y-%m-%d')
            mes = hoje.month
            total_servicos = 0
            servicos = 0
            dinheiro = 0
            debito = 0
            credito = 0
            aberto = 0
            desmarcado = 0
            agendamento = 0
            contas = 0
            retiradas = 0
            entradas = 0 
            saidas = 0
            total_geral = 0
            n_dinheiro = 0
            n_debito = 0
            n_credito = 0
            n_aberto = 0
            n_desmarcado = 0
            n_agendamento = 0
            n_contas = 0
            n_retiradas = 0
            n_entradas = 0
            n_saidas = 0
            
            for r in caixa_geral.objects.filter(operacao=2, descricao__icontains="Retirada -", data__month=mes).all():
                retiradas = retiradas + r.valor_operacao
                n_retiradas = n_retiradas + 1
            for e in caixa_geral.objects.filter(operacao=1, descricao__icontains="Entrada -", data__month=mes).all():
                    entradas = entradas + e.valor_operacao
                    n_entradas = n_entradas + 1
            for c in conta.objects.filter(estado=2, data_pagamento__month=mes).all():
                contas = contas + c.valor
                n_contas = n_contas + 1
            for d in agenda.objects.filter(pagamento=1, data__month=mes).all():
                dinheiro = dinheiro + d.total
                n_dinheiro = n_dinheiro + 1
            for s in agenda.objects.filter(pagamento=2, data__month=mes).all():
                debito = debito + s.total
                n_debito = n_debito + 1
            for s in agenda.objects.filter(pagamento=3, data__month=mes).all():
                credito = credito + s.total
                n_credito = n_credito + 1
            for s in agenda.objects.filter(pagamento=4, data__month=mes).all():
                aberto = aberto + s.total
                n_aberto = n_aberto + 1
            for s in agenda.objects.filter(pagamento=5, data__month=mes).all():
                desmarcado = desmarcado + s.total
                n_desmarcado = n_desmarcado + 1
            n_saidas = n_retiradas + n_contas
            saidas = retiradas + contas
            n_agendamento = n_dinheiro + n_credito + n_debito
            agendamento = dinheiro + debito + credito 
            total_geral = (agendamento + entradas) - saidas
            if request.method == 'POST' and request.POST.get('data_inicio') != None and request.POST.get('data_fim') != None:
                data_inicio = request.POST.get('data_inicio')
                data_fim = request.POST.get('data_fim')
                total_servicos = 0
                servicos = 0
                dinheiro = 0
                debito = 0
                credito = 0
                aberto = 0
                desmarcado = 0
                agendamento = 0
                contas = 0
                retiradas = 0
                entradas = 0
                saidas = 0
                total_geral = 0
                n_dinheiro = 0
                n_debito = 0
                n_credito = 0
                n_aberto = 0
                n_desmarcado = 0
                n_agendamento = 0
                n_contas = 0
                n_retiradas = 0
                n_entradas = 0
                n_saidas = 0
                for r in caixa_geral.objects.filter(operacao=2, descricao__icontains="Retirada -", data__range=(data_inicio,data_fim)).all():
                    retiradas = retiradas + r.valor_operacao
                    n_retiradas = n_retiradas + 1
                for e in caixa_geral.objects.filter(operacao=1, descricao__icontains="Entrada -", data__range=(data_inicio,data_fim)).all():
                    entradas = entradas + e.valor_operacao
                    n_entradas = n_entradas + 1
                for c in conta.objects.filter(estado=2, data_pagamento__range=(data_inicio,data_fim)).all():
                    contas = contas + c.valor
                    n_contas = n_contas + 1
                for d in agenda.objects.filter(pagamento=1, data__range=(data_inicio,data_fim)).all():
                    dinheiro = dinheiro + d.total
                    n_dinheiro = n_dinheiro + 1
                for s in agenda.objects.filter(pagamento=2, data__range=(data_inicio,data_fim)).all():
                    debito = debito + s.total
                    n_debito = n_debito + 1
                for s in agenda.objects.filter(pagamento=3, data__range=(data_inicio,data_fim)).all():
                    credito = credito + s.total
                    n_credito = n_credito + 1
                for s in agenda.objects.filter(pagamento=4, data__range=(data_inicio,data_fim)).all():
                    aberto = aberto + s.total
                    n_aberto = n_aberto + 1
                for s in agenda.objects.filter(pagamento=5, data__range=(data_inicio,data_fim)).all():
                    desmarcado = desmarcado + s.total
                    n_desmarcado = n_desmarcado + 1
                n_saidas = n_retiradas + n_contas
                saidas = retiradas + contas
                n_agendamento = n_dinheiro + n_credito + n_debito
                agendamento = dinheiro + debito + credito 
                total_geral = (agendamento + agendamento) - saidas
                return render(request, 'lavajato_caixa/caixa_balanco.html', {'title':'Balanco caixa', 'dinheiro':dinheiro, 'n_dinheiro':n_dinheiro, 'debito':debito, 'n_debito':n_debito, 'credito':credito, 'n_credito':n_credito, 'aberto':aberto, 'n_aberto':n_aberto, 'desmarcado':desmarcado, 'n_desmarcado':n_desmarcado, 'n_agendamento':n_agendamento, 'agendamento':agendamento, 'n_contas':n_contas, 'contas':contas, 'n_retiradas':n_retiradas, 'retiradas':retiradas, 'n_saidas':n_saidas, 'saidas':saidas, 'total_geral':total_geral, 'hj':hj, 'n_entradas':n_entradas, 'entradas': entradas})

            return render(request, 'lavajato_caixa/caixa_balanco.html', {'title':'Balanco caixa', 'dinheiro':dinheiro, 'n_dinheiro':n_dinheiro, 'debito':debito, 'n_debito':n_debito, 'credito':credito, 'n_credito':n_credito, 'aberto':aberto, 'n_aberto':n_aberto, 'desmarcado':desmarcado, 'n_desmarcado':n_desmarcado, 'n_agendamento':n_agendamento, 'agendamento':agendamento, 'n_contas':n_contas, 'contas':contas, 'n_retiradas':n_retiradas, 'retiradas':retiradas, 'n_saidas':n_saidas, 'saidas':saidas, 'total_geral':total_geral, 'hj':hj, 'n_entradas':n_entradas, 'entradas': entradas})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})