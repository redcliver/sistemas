from django.shortcuts import render
from django.utils import timezone
import datetime
from .models import conta
from lavajato_agenda.models import conta_parcelada
from lavajato_caixa.models import caixa_geral
from datetime import datetime
from datetime import timedelta
from decimal import Decimal

# Create your views here.
def lavajato_contas(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            if request.method == 'POST' and request.POST.get('nome') != None:
                nome = request.POST.get('nome')
                valor = request.POST.get('valor')
                data_venc = request.POST.get('data_venc')
                fixa = request.POST.get('fixa')
                nova_conta = conta(nome=nome, valor=valor, fixa=fixa, data_venc=data_venc, estado=1)
                nova_conta.save()
                msg = nome +" cadastrado(a) com sucesso!"
                return render(request, 'lavajato_contas/conta_novo.html', {'title':'Nova Conta', 'msg':msg})
            return render(request, 'lavajato_contas/conta_novo.html', {'title':'Nova Conta'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def busca(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            contas = conta.objects.all().order_by('data_venc')
            if request.method == 'POST' and request.POST.get('conta_id') != None:
                conta_id = request.POST.get('conta_id')
                conta_obj = conta.objects.get(id=conta_id)
                return render(request, 'lavajato_contas/conta_visualizar.html', {'title':'Visualizar Conta', 'conta_obj':conta_obj})
            return render(request, 'lavajato_contas/conta_busca.html', {'title':'Buscar Conta', 'contas':contas})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def edita(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            contas = conta.objects.filter(estado=1).all().order_by('nome')
            if request.method == 'POST' and request.POST.get('conta_id') != None:
                conta_id = request.POST.get('conta_id')
                conta_obj = conta.objects.get(id=conta_id)
                return render(request, 'lavajato_contas/conta_edita.html', {'title':'Visualizar Conta', 'conta_obj':conta_obj})
            return render(request, 'lavajato_contas/conta_busca_edita.html', {'title':'Editar Conta', 'contas':contas})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def salva(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            if request.method == 'POST' and request.POST.get('nome') != None:
                conta_id = request.POST.get('conta_id')
                conta_obj = conta.objects.get(id=conta_id)
                nome = request.POST.get('nome')
                valor = request.POST.get('valor')
                valor = Decimal(valor)
                data_venc = request.POST.get('data_venc')
                estado = request.POST.get('estado')
                fixa = request.POST.get('fixa')
                conta_obj.nome = nome
                conta_obj.valor = valor
                conta_obj.data_venc = data_venc
                conta_obj.estado = estado
                conta_obj.fixa = fixa
                conta_obj.save()
                msg = nome +" editado(a) com sucesso!"
                contas = conta.objects.all().order_by('data_venc')
                return render(request, 'lavajato_contas/conta_busca_edita.html', {'title':'Editar Conta', 'msg':msg, 'contas':contas})
            return render(request, 'lavajato_contas/conta_busca_edita.html', {'title':'Editar Conta'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def pagar(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            contas = conta.objects.filter(estado=1).all().order_by('data_venc')
            if request.method == 'POST' and request.POST.get('conta_id') != None:
                hoje = timezone.now()
                conta_id = request.POST.get('conta_id')
                conta_obj = conta.objects.get(id=conta_id)
                if conta_obj.fixa == 'Nao':
                    conta_obj.data_pagamento = hoje
                    conta_obj.estado = 2
                    conta_obj.save()
                    caixa = caixa_geral.objects.latest('id')
                    ultimo_id = conta_obj.id
                    novo_total = caixa.total - conta_obj.valor
                    valor = conta_obj.valor
                    desc = "Pagamento da conta : " + str(conta_obj.nome)
                    nova_saida = caixa_geral(operacao=2, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                    nova_saida.save()
                    msg = conta_obj.nome + " pago(a) com sucesso!"
                    return render(request, 'lavajato_contas/conta_pagar.html', {'title':'Pagar Conta', 'contas':contas, 'msg':msg})
                if conta_obj.fixa == 'Sim':
                    conta_obj.data_pagamento = hoje
                    conta_obj.estado = 2
                    conta_obj.save()
                    caixa = caixa_geral.objects.latest('id')
                    ultimo_id = conta_obj.id
                    novo_total = caixa.total - conta_obj.valor
                    valor = conta_obj.valor
                    desc = "Pagamento da conta : " + str(conta_obj.nome)
                    nova_saida = caixa_geral(operacao=2, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                    nova_saida.save()
                    nome = conta_obj.nome
                    data_venc = conta_obj.data_venc + timedelta(days=30)
                    fixa = "Sim"
                    nova_conta = conta(nome=nome, valor=valor, fixa=fixa, data_venc=data_venc, estado=1)
                    nova_conta.save()
                    msg = conta_obj.nome + " pago(a) e agendada com sucesso!"
                    return render(request, 'lavajato_contas/conta_pagar.html', {'title':'Pagar Conta', 'contas':contas, 'msg':msg})
            return render(request, 'lavajato_contas/conta_pagar.html', {'title':'Pagar Conta', 'contas':contas})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})


def receber(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            msg = "Contas recebidas com sucesso."
            return render(request, 'lavajato_home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def relatorio_pagar(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            data_inicio = datetime.now().strftime('%Y-%m-%d')
            data_fim = datetime.now().strftime('%Y-%m-%d')
            mes = datetime.now().month
            t_aberta = 0
            n_aberta = 0
            t_paga = 0
            n_paga = 0
            n_contas = 0
            contas_all = conta.objects.filter(data_venc__month=mes).all()
            for a in conta.objects.filter(estado=1, data_venc__month=mes).all():
                    t_aberta = t_aberta + a.valor
                    n_aberta = n_aberta + 1
            for b in conta.objects.filter(estado=2, data_venc__month=mes).all():
                    t_paga = t_paga + b.valor
                    n_paga = n_paga + 1
            n_contas = n_aberta + n_paga
            t_contas = t_aberta + t_paga
            if request.method == 'POST' and request.POST.get('data_inicio') != None and request.POST.get('data_fim') != None:
                data_inicio = request.POST.get('data_inicio')
                data_fim = request.POST.get('data_fim')
                t_aberta = 0
                n_aberta = 0
                t_paga = 0
                n_paga = 0
                n_contas = 0
                contas_all = conta.objects.filter(data_venc__range=(data_inicio,data_fim)).all()
                for a in conta.objects.filter(estado=1, data_venc__range=(data_inicio,data_fim)).all():
                        t_aberta = t_aberta + a.valor
                        n_aberta = n_aberta + 1
                for b in conta.objects.filter(estado=2, data_venc__range=(data_inicio,data_fim)).all():
                        t_paga = t_paga + b.valor
                        n_paga = n_paga + 1
                n_contas = n_aberta + n_paga
                t_contas = t_aberta + t_paga
                return render(request, 'lavajato_contas/conta_relatorio_pagar.html', {'title':'Relatorio Contas a Pagar', 'data_inicio':data_inicio, 'data_fim':data_fim, 'contas_all':contas_all, 't_aberta':t_aberta, 'n_aberta':n_aberta, 't_paga':t_paga, 'n_paga':n_paga, 't_contas':t_contas, 'n_contas':n_contas})
            return render(request, 'lavajato_contas/conta_relatorio_pagar.html', {'title':'Relatorio Contas a Pagar', 'data_inicio':data_inicio, 'data_fim':data_fim, 'contas_all':contas_all, 't_aberta':t_aberta, 'n_aberta':n_aberta, 't_paga':t_paga, 'n_paga':n_paga, 't_contas':t_contas, 'n_contas':n_contas})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})