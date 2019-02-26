from django.shortcuts import render
from .models import caixa_geral
from lavajato_agenda.models import agenda, servico_item, pagamento
from lavajato_controle.models import funcionario, servico, conta_empresa
from lavajato_contas.models import conta
from django.utils import timezone
import datetime
from decimal import *
from datetime import datetime
from datetime import timedelta

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
            data_limite = datetime.now() + timezone.timedelta(days=1)
            t_caixa = 0
            total_retirada = 0
            for y in caixa_geral.objects.filter(data__lte=(data_limite)).filter(operacao=2, descricao__startswith="Retirada -").all():
                total_retirada = total_retirada + y.valor_operacao
            for z in caixa_geral.objects.filter(data__lte=(data_limite)).filter(operacao=2, descricao__startswith="Pagamento conta").all():
                total_retirada = total_retirada + z.valor_operacao
            for w in pagamento.objects.filter(data__lte=(data_limite), tipo=1).all():
                t_caixa = t_caixa + w.valor
            t_caixa = t_caixa - total_retirada
            if request.method == 'POST' and request.POST.get('desc') != None:
                desc = request.POST.get('desc')
                valor = request.POST.get('valor')
                caixa = caixa_geral.objects.latest('id')
                data_limite = datetime.now() + timezone.timedelta(days=1)
                t_caixa = 0
                total_retirada = 0
                for y in caixa_geral.objects.filter(data__lte=(data_limite)).filter(operacao=2, descricao__startswith="Retirada -").all():
                    total_retirada = total_retirada + y.valor_operacao
                for z in caixa_geral.objects.filter(data__lte=(data_limite)).filter(operacao=2, descricao__startswith="Pagamento conta").all():
                    total_retirada = total_retirada + z.valor_operacao
                for w in pagamento.objects.filter(data__lte=(data_limite), tipo=1).all():
                    t_caixa = t_caixa + w.valor
                t_caixa = t_caixa - total_retirada
                ultimo_id = caixa.id_operacao
                ultimo_id = int(ultimo_id) + 1
                desc = "Entrada - "+desc
                novo_total = caixa.total + Decimal(valor)
                nova_entrada = caixa_geral(operacao=1, tipo=1, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                nova_entrada.save()
                msg = "Entrada registrada com sucesso!"
                return render(request, 'lavajato_caixa/caixa_entrada.html', {'title':'Entrada', 'msg':msg,'t_caixa':t_caixa})
            return render(request, 'lavajato_caixa/caixa_entrada.html', {'title':'Entrada', 't_caixa':t_caixa})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def saida(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            data_limite = datetime.now() + timezone.timedelta(days=1)
            t_caixa = 0
            total_retirada = 0
            for y in caixa_geral.objects.filter(data__lte=(data_limite)).filter(operacao=2, descricao__startswith="Retirada -").all():
                total_retirada = total_retirada + y.valor_operacao
            for z in caixa_geral.objects.filter(data__lte=(data_limite)).filter(operacao=2, descricao__startswith="Pagamento conta").all():
                total_retirada = total_retirada + z.valor_operacao
            for w in pagamento.objects.filter(data__lte=(data_limite), tipo=1).all():
                t_caixa = t_caixa + w.valor
            t_caixa = t_caixa - total_retirada
            if request.method == 'POST' and request.POST.get('desc') != None:
                desc = request.POST.get('desc')
                valor = request.POST.get('valor')
                caixa = caixa_geral.objects.latest('id')
                data_limite = datetime.now() + timezone.timedelta(days=1)
                t_caixa = 0
                total_retirada = 0
                for y in caixa_geral.objects.filter(data__lte=(data_limite)).filter(operacao=2, descricao__startswith="Retirada -").all():
                    total_retirada = total_retirada + y.valor_operacao
                for z in caixa_geral.objects.filter(data__lte=(data_limite)).filter(operacao=2, descricao__startswith="Pagamento conta").all():
                    total_retirada = total_retirada + z.valor_operacao
                for w in pagamento.objects.filter(data__lte=(data_limite), tipo=1).all():
                    t_caixa = t_caixa + w.valor
                t_caixa = t_caixa - total_retirada
                ultimo_id = caixa.id_operacao
                ultimo_id = int(ultimo_id) + 1
                desc = "Retirada - " + desc
                novo_total = caixa.total - Decimal(valor)
                nova_saida = caixa_geral(operacao=2, tipo=1, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                nova_saida.save()
                msg = "Saida registrada com sucesso!"
                return render(request, 'lavajato_caixa/caixa_saida.html', {'title':'Saida', 'msg':msg,'t_caixa':t_caixa})
            return render(request, 'lavajato_caixa/caixa_saida.html', {'title':'Saida','t_caixa':t_caixa})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def conferencia(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            data = datetime.now().strftime('%Y-%m-%d')
            data_limite = datetime.now() + timezone.timedelta(days=1)
            caixas = caixa_geral.objects.filter(data__date=(data)).order_by('data')
            caixa = caixa_geral.objects.latest('id')
            total = caixa.total
            t_dinheiro = 0
            t_debito = 0
            t_credito = 0
            t_elodebito = 0
            t_elocredito = 0
            t_retirada = 0
            total_retirada = 0
            total_din = 0
            t_caixa = 0
            for p in pagamento.objects.filter(data__date=(data)).all():
                if p.tipo == '1':
                    t_dinheiro = t_dinheiro + p.valor
                if p.tipo == '2':
                    t_debito = t_debito + p.valor
                if p.tipo == '3':
                    t_credito = t_credito + p.valor
                if p.tipo == '4':
                    t_elodebito = t_elodebito + p.valor
                if p.tipo == '5':
                    t_elocredito = t_elocredito + p.valor
            for r in caixa_geral.objects.filter(data__date=(data)).filter(operacao=2, descricao__startswith="Retirada -").all():
                t_retirada = t_retirada + r.valor_operacao
            for s in caixa_geral.objects.filter(data__date=(data)).filter(operacao=2, descricao__startswith="Pagamento conta").all():
                t_retirada = t_retirada + s.valor_operacao
            for y in caixa_geral.objects.filter(data__lte=(data_limite)).filter(operacao=2, descricao__startswith="Retirada -").all():
                total_retirada = total_retirada + y.valor_operacao
            for z in caixa_geral.objects.filter(data__lte=(data_limite)).filter(operacao=2, descricao__startswith="Pagamento conta").all():
                total_retirada = total_retirada + z.valor_operacao
            for w in pagamento.objects.filter(data__lte=(data_limite), tipo=1).all():
                t_caixa = t_caixa + w.valor
            t_caixa = t_caixa - total_retirada
            if request.method == 'POST' and request.POST.get('data') != None:
                data = request.POST.get('data')
                data_limite = datetime.strptime(data, '%Y-%m-%d')
                data_limite = data_limite + timezone.timedelta(days=1)
                caixas = caixa_geral.objects.filter(data__date=(data))
                t_dinheiro = 0
                t_debito = 0
                t_credito = 0
                t_elodebito = 0
                t_elocredito = 0
                t_retirada = 0
                total_retirada = 0
                total_din = 0
                t_caixa = 0
                for p in pagamento.objects.filter(data__date=(data)).all():
                    if p.tipo == '1':
                        t_dinheiro = t_dinheiro + p.valor
                    if p.tipo == '2':
                        t_debito = t_debito + p.valor
                    if p.tipo == '3':
                        t_credito = t_credito + p.valor
                    if p.tipo == '4':
                        t_elodebito = t_elodebito + p.valor
                    if p.tipo == '5':
                        t_elocredito = t_elocredito + p.valor
                for r in caixa_geral.objects.filter(data__date=(data)).filter(operacao=2, descricao__startswith="Retirada -").all():
                    t_retirada = t_retirada + r.valor_operacao
                for s in caixa_geral.objects.filter(data__date=(data)).filter(operacao=2, descricao__startswith="Pagamento conta").all():
                    t_retirada = t_retirada + s.valor_operacao
                for y in caixa_geral.objects.filter(data__lte=data_limite).filter(operacao=2, descricao__startswith="Retirada -").all():
                    total_retirada = total_retirada + y.valor_operacao
                for z in caixa_geral.objects.filter(data__lte=data_limite).filter(operacao=2, descricao__startswith="Pagamento conta").all():
                    total_retirada = total_retirada + z.valor_operacao
                for w in pagamento.objects.filter(data__lte=data_limite, tipo=1).all():
                    t_caixa = t_caixa + w.valor
                t_caixa = t_caixa - total_retirada
                return render(request, 'lavajato_caixa/caixa_conferencia.html', {'title':'Conferencia', 'caixas':caixas, 'data':data, 'total':total, 't_credito':t_credito, 't_debito':t_debito, 't_elocredito':t_elocredito, 't_elodebito':t_elodebito, 't_dinheiro':t_dinheiro, 't_caixa':t_caixa, 't_retirada':t_retirada})
            return render(request, 'lavajato_caixa/caixa_conferencia.html', {'title':'Conferencia', 'caixas':caixas, 'data':data, 'total':total, 't_credito':t_credito, 't_debito':t_debito, 't_elocredito':t_elocredito, 't_elodebito':t_elodebito, 't_dinheiro':t_dinheiro, 't_caixa':t_caixa, 't_retirada':t_retirada})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def fechar(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            data = datetime.now().strftime('%Y-%m-%d')
            data_limite = datetime.now() + timezone.timedelta(days=1)
            caixa = caixa_geral.objects.latest('id')            
            total = caixa.total

            t_dinheiro = 0
            t_debito = 0
            t_credito = 0
            t_elodebito = 0
            t_elocredito = 0
            t_retirada = 0
            total_retirada = 0
            total_din = 0
            t_caixa = 0
            for p in pagamento.objects.filter(data__date=(data)).all():
                if p.tipo == '1':
                    t_dinheiro = t_dinheiro + p.valor
                if p.tipo == '2':
                    t_debito = t_debito + p.valor
                if p.tipo == '3':
                    t_credito = t_credito + p.valor
                if p.tipo == '4':
                    t_elodebito = t_elodebito + p.valor
                if p.tipo == '5':
                    t_elocredito = t_elocredito + p.valor
            for r in caixa_geral.objects.filter(data__date=(data)).filter(operacao=2, descricao__startswith="Retirada -").all():
                t_retirada = t_retirada + r.valor_operacao
            for s in caixa_geral.objects.filter(data__date=(data)).filter(operacao=2, descricao__startswith="Pagamento conta").all():
                t_retirada = t_retirada + s.valor_operacao
            for y in caixa_geral.objects.filter(data__lte=data_limite).filter(operacao=2, descricao__startswith="Retirada -").all():
                total_retirada = total_retirada + y.valor_operacao
            for z in caixa_geral.objects.filter(data__lte=data_limite).filter(operacao=2, descricao__startswith="Pagamento conta").all():
                total_retirada = total_retirada + z.valor_operacao
            for w in pagamento.objects.filter(data__lte=data_limite, tipo=1).all():
                t_caixa = t_caixa + w.valor
            t_caixa = t_caixa - total_retirada
            if request.method == 'POST' and request.POST.get('valor') != None:
                data = datetime.now().strftime('%Y-%m-%d')
                data_limite = datetime.strptime(data, '%Y-%m-%d')
                data_limite = data_limite + timezone.timedelta(days=1)
                caixas = caixa_geral.objects.filter(data__date=(data))
                desc = "Retirada - Fechamento de caixa"
                valor = request.POST.get('valor')
                valor_1 = request.POST.get('valor')
                t_cartao = t_credito + t_debito
                valor_fechamento = Decimal(valor)
                caixa = caixa_geral.objects.latest('id')
                ultimo_id = caixa.id_operacao
                ultimo_id = int(ultimo_id) + 1
                novo_total = caixa.total - valor_fechamento
                nova_saida = caixa_geral(operacao=2, tipo=1, id_operacao=ultimo_id, valor_operacao=valor_fechamento, descricao=desc, total=novo_total)
                nova_saida.save()
                ultima_conta = conta_empresa.objects.latest('id')
                desc1 = "Fechamento do caixa dia " + str(nova_saida.data.strftime('%d/%m/%Y'))
                novo_total_conta = ultima_conta.total + Decimal(valor_1)
                nova_entrada_conta = conta_empresa(operacao=1, id_operacao=nova_saida.id, valor_operacao=valor_1, descricao=desc1, total=novo_total_conta)
                nova_entrada_conta.save()
                msg = "Caixa fechado com sucesso, retirada de R$ " + str(valor_1)
                t_dinheiro = 0
                t_debito = 0
                t_credito = 0
                t_elodebito = 0
                t_elocredito = 0
                t_retirada = 0
                total_retirada = 0
                total_din = 0
                t_caixa = 0
                for p in pagamento.objects.filter(data__date=(data)).all():
                    if p.tipo == '1':
                        t_dinheiro = t_dinheiro + p.valor
                    if p.tipo == '2':
                        t_debito = t_debito + p.valor
                    if p.tipo == '3':
                        t_credito = t_credito + p.valor
                    if p.tipo == '4':
                        t_elodebito = t_elodebito + p.valor
                    if p.tipo == '5':
                        t_elocredito = t_elocredito + p.valor
                for r in caixa_geral.objects.filter(data__date=(data)).filter(operacao=2, descricao__startswith="Retirada -").all():
                    t_retirada = t_retirada + r.valor_operacao
                for s in caixa_geral.objects.filter(data__date=(data)).filter(operacao=2, descricao__startswith="Pagamento conta").all():
                    t_retirada = t_retirada + s.valor_operacao
                for y in caixa_geral.objects.filter(data__lte=data_limite).filter(operacao=2, descricao__startswith="Retirada -").all():
                    total_retirada = total_retirada + y.valor_operacao
                for z in caixa_geral.objects.filter(data__lte=data_limite).filter(operacao=2, descricao__startswith="Pagamento conta").all():
                    total_retirada = total_retirada + z.valor_operacao
                for w in pagamento.objects.filter(data__lte=data_limite, tipo=1).all():
                    t_caixa = t_caixa + w.valor
                t_caixa = t_caixa - total_retirada
                return render(request, 'lavajato_caixa/caixa_conferencia.html', {'title':'Conferencia', 'caixas':caixas, 'data':data, 'total':total, 't_credito':t_credito, 't_debito':t_debito, 't_elocredito':t_elocredito, 't_elodebito':t_elodebito, 't_dinheiro':t_dinheiro, 't_caixa':t_caixa, 't_retirada':t_retirada})
            return render(request, 'lavajato_caixa/caixa_fechar.html', {'title':'Fechar caixa', 'data':data, 't_credito':t_credito, 't_debito':t_debito, 't_elocredito':t_elocredito, 't_elodebito':t_elodebito, 't_dinheiro':t_dinheiro, 't_caixa':t_caixa, 't_retirada':t_retirada})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def balanco(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = datetime.now()
            data_inicio = datetime.now().strftime('%Y-%m-%d')
            data_fim = datetime.now() + timedelta(days=-30)
            data_fim = data_fim.strftime('%Y-%m-%d')
            mes = hoje.month
            total_servicos = 0
            servicos = 0
            pago = 0
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
            n_pago = 0
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
            for d in agenda.objects.filter(pag=1, data__month=mes).all():
                aberto = aberto + d.total
                n_aberto = n_aberto + 1
            for s in agenda.objects.filter(pag=3, data__month=mes).all():
                pago = pago + s.total
                n_pago = n_pago + 1
            n_saidas = n_retiradas + n_contas
            saidas = retiradas + contas
            n_agendamento = n_pago
            agendamento = pago
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
                
                n_saidas = n_retiradas + n_contas
                saidas = retiradas + contas
                n_agendamento = n_dinheiro + n_credito + n_debito
                agendamento = dinheiro + debito + credito 
                total_geral = (agendamento + entradas) - saidas
                return render(request, 'lavajato_caixa/caixa_balanco.html', {'title':'Balanco caixa', 'data_inicio':data_inicio, 'data_fim':data_fim, 'dinheiro':dinheiro, 'n_dinheiro':n_dinheiro, 'debito':debito, 'n_debito':n_debito, 'credito':credito, 'n_credito':n_credito, 'aberto':aberto, 'n_aberto':n_aberto, 'desmarcado':desmarcado, 'n_desmarcado':n_desmarcado, 'n_agendamento':n_agendamento, 'agendamento':agendamento, 'n_contas':n_contas, 'contas':contas, 'n_retiradas':n_retiradas, 'retiradas':retiradas, 'n_saidas':n_saidas, 'saidas':saidas, 'total_geral':total_geral, 'n_entradas':n_entradas, 'entradas': entradas})
            if request.method == 'POST' and request.POST.get('data_inicio') == request.POST.get('data_fim'):
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
                for r in caixa_geral.objects.filter(operacao=2, descricao__icontains="Retirada -", data__date=(data_inicio)).all():
                    retiradas = retiradas + r.valor_operacao
                    n_retiradas = n_retiradas + 1
                for e in caixa_geral.objects.filter(operacao=1, descricao__icontains="Entrada -", data__date=(data_inicio)).all():
                    entradas = entradas + e.valor_operacao
                    n_entradas = n_entradas + 1
                for c in conta.objects.filter(estado=2, data_pagamento__date=(data_inicio)).all():
                    contas = contas + c.valor
                    n_contas = n_contas + 1
                for d in agenda.objects.filter(pagamento=1, data__date=(data_inicio)).all():
                    dinheiro = dinheiro + d.total
                    n_dinheiro = n_dinheiro + 1
                for s in agenda.objects.filter(pagamento=2, data__date=(data_inicio)).all():
                    debito = debito + s.total
                    n_debito = n_debito + 1
                for s in agenda.objects.filter(pagamento=3, data__date=(data_inicio)).all():
                    credito = credito + s.total
                    n_credito = n_credito + 1
                for s in agenda.objects.filter(pagamento=4, data__date=(data_inicio)).all():
                    aberto = aberto + s.total
                    n_aberto = n_aberto + 1
                for s in agenda.objects.filter(pagamento=5, data__date=(data_inicio)).all():
                    desmarcado = desmarcado + s.total
                    n_desmarcado = n_desmarcado + 1
                n_saidas = n_retiradas + n_contas
                saidas = retiradas + contas
                n_agendamento = n_dinheiro + n_credito + n_debito
                agendamento = dinheiro + debito + credito 
                total_geral = (agendamento + entradas) - saidas
                return render(request, 'lavajato_caixa/caixa_balanco.html', {'title':'Balanco caixa', 'data_inicio':data_inicio, 'data_fim':data_fim, 'dinheiro':dinheiro, 'n_dinheiro':n_dinheiro, 'debito':debito, 'n_debito':n_debito, 'credito':credito, 'n_credito':n_credito, 'aberto':aberto, 'n_aberto':n_aberto, 'desmarcado':desmarcado, 'n_desmarcado':n_desmarcado, 'n_agendamento':n_agendamento, 'agendamento':agendamento, 'n_contas':n_contas, 'contas':contas, 'n_retiradas':n_retiradas, 'retiradas':retiradas, 'n_saidas':n_saidas, 'saidas':saidas, 'total_geral':total_geral, 'n_entradas':n_entradas, 'entradas': entradas})

            return render(request, 'lavajato_caixa/caixa_balanco.html', {'title':'Balanco caixa','data_inicio':data_inicio, 'data_fim':data_fim, 'pago':pago, 'n_pago':n_pago, 'aberto':aberto, 'n_aberto':n_aberto, 'desmarcado':desmarcado, 'n_desmarcado':n_desmarcado, 'n_agendamento':n_agendamento, 'agendamento':agendamento, 'n_contas':n_contas, 'contas':contas, 'n_retiradas':n_retiradas, 'retiradas':retiradas, 'n_saidas':n_saidas, 'saidas':saidas, 'total_geral':total_geral, 'n_entradas':n_entradas, 'entradas': entradas})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
