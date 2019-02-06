from django.shortcuts import render
from django.utils import timezone
import datetime
from .models import conta
from lavajato_caixa.models import caixa_geral
from lavajato_agenda.models import parcela
from lavajato_controle.models import conta_empresa
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
            data_inicio = datetime.now().strftime('%Y-%m-%d')
            data_fim = datetime.now().strftime('%Y-%m-%d')
            contas_all = conta.objects.filter(data_venc__range=(data_inicio,data_fim)).all()
            if request.method == 'GET' and request.GET.get('data_inicio') != None and request.GET.get('data_fim') != None:
                data_inicio = request.GET.get('data_inicio')
                data_fim = request.GET.get('data_fim')
                contas_all = conta.objects.filter(data_venc__range=(data_inicio,data_fim)).all()
                return render(request, 'lavajato_contas/conta_busca.html', {'title':'Buscar Conta', 'contas_all':contas_all, 'data_inicio':data_inicio, 'data_fim':data_fim})

            if request.method == 'POST' and request.POST.get('conta_id') != None:
                conta_id = request.POST.get('conta_id')
                conta_obj = conta.objects.get(id=conta_id)
                return render(request, 'lavajato_contas/conta_visualizar.html', {'title':'Visualizar Conta', 'conta_obj':conta_obj})
            return render(request, 'lavajato_contas/conta_busca.html', {'title':'Buscar Conta', 'contas_all':contas_all, 'data_inicio':data_inicio, 'data_fim':data_fim})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def edita(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            contas = conta.objects.filter(estado=1).all().order_by('data_venc')
            if request.method == 'POST' and request.POST.get('conta_id') != None:
                conta_id = request.POST.get('conta_id')
                conta_obj = conta.objects.get(id=conta_id)
                dec_valor = conta_obj.valor
                dec_valor = Decimal(dec_valor)
                return render(request, 'lavajato_contas/conta_edita.html', {'title':'Visualizar Conta', 'conta_obj':conta_obj, 'dec_valor':dec_valor})
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
                data_venc = request.POST.get('data_venc')
                estado = request.POST.get('estado')
                fixa = request.POST.get('fixa')
                conta_obj.nome = nome
                if valor != None or valor != '':
                    conta_obj.valor = Decimal(valor)
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
            data_inicio = datetime.now() + timedelta(days=-1)
            data_inicio = data_inicio.strftime('%Y-%m-%d')
            data_fim = datetime.now().strftime('%Y-%m-%d')
            hoje = datetime.now()
            contas_all = conta.objects.filter(data_venc__lte=data_inicio).all()
            if request.method == 'GET' and request.GET.get('data_inicio') != None and request.GET.get('data_fim') != None:
                data_inicio = request.GET.get('data_inicio')
                data_fim = request.GET.get('data_fim')
                contas_all = conta.objects.filter(data_venc__range=(data_inicio,data_fim)).all()
                return render(request, 'lavajato_contas/conta_pagar.html', {'title':'Buscar Conta', 'contas_all':contas_all, 'data_inicio':data_inicio, 'data_fim':data_fim})
            if request.method == 'POST' and request.POST.get('conta_id') != None:
                data_inicio = request.POST.get('data_inicio')
                data_fim = request.POST.get('data_fim')
                conta_id = request.POST.get('conta_id')
                conta_obj = conta.objects.get(id=conta_id)
                if conta_obj.fixa == 'Nao':
                    conta_obj.data_pagamento = hoje
                    conta_obj.estado = 2
                    conta_obj.save()
                    conta_empresa_obj = conta_empresa.objects.latest('id')
                    ultimo_id = conta_obj.id
                    novo_total = conta_empresa_obj.total - conta_obj.valor
                    valor = conta_obj.valor
                    desc = "Pagamento da conta : " + str(conta_obj.nome)
                    nova_saida = conta_empresa(operacao=2, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                    nova_saida.save()
                    msg = conta_obj.nome + " pago(a) com sucesso!"
                    contas_all = conta.objects.filter(data_venc__range=(data_inicio,data_fim)).all()
                    return render(request, 'lavajato_contas/conta_pagar.html', {'title':'Pagar Conta', 'contas_all':contas_all, 'data_inicio':data_inicio, 'data_fim':data_fim, 'msg':msg})
                if conta_obj.fixa == 'Sim':
                    conta_obj.data_pagamento = hoje
                    conta_obj.estado = 2
                    conta_obj.save()
                    conta_empresa_obj = conta_empresa.objects.latest('id')
                    ultimo_id = conta_obj.id
                    novo_total = conta_empresa_obj.total - conta_obj.valor
                    valor = conta_obj.valor
                    desc = "Pagamento da conta : " + str(conta_obj.nome)
                    nova_saida = conta_empresa(operacao=2, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                    nova_saida.save()
                    nome = conta_obj.nome
                    data_venc = conta_obj.data_venc + timedelta(days=30)
                    fixa = "Sim"
                    nova_conta = conta(nome=nome, valor=valor, fixa=fixa, data_venc=data_venc, estado=1)
                    nova_conta.save()
                    msg = conta_obj.nome + " pago(a) e agendada com sucesso!"
                    contas_all = conta.objects.filter(data_venc__range=(data_inicio,data_fim)).all()
                    return render(request, 'lavajato_contas/conta_pagar.html', {'title':'Pagar Conta', 'contas_all':contas_all, 'data_inicio':data_inicio, 'data_fim':data_fim, 'msg':msg})

                return render(request, 'lavajato_contas/conta_pagar.html', {'title':'Pagar Conta', 'conta_obj':conta_obj})
            return render(request, 'lavajato_contas/conta_pagar.html', {'title':'Pagar Conta', 'contas_all':contas_all, 'data_inicio':data_inicio, 'data_fim':data_fim})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def conta_receber(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            data_inicio = datetime.now().strftime('%Y-%m-%d')
            data_fim = datetime.now().strftime('%Y-%m-%d')
            hoje = datetime.now()
            parcela_all = parcela.objects.filter(data__range=(data_inicio,data_fim)).all().order_by('data')
            if request.method == 'GET' and request.GET.get('data_inicio') != None and request.GET.get('data_fim') != None:
                data_inicio = request.GET.get('data_inicio')
                data_fim = request.GET.get('data_fim')
                parcela_all = parcela.objects.filter(data__range=(data_inicio,data_fim)).all().order_by('data')
                return render(request, 'lavajato_contas/conta_receber.html', {'title':'Receber Conta', 'parcela_all':parcela_all, 'data_inicio':data_inicio, 'data_fim':data_fim})
            return render(request, 'lavajato_contas/conta_receber.html', {'title':'Receber Conta', 'parcela_all':parcela_all, 'data_inicio':data_inicio, 'data_fim':data_fim})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def confirmar_recebimento(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            data_inicio = datetime.now().strftime('%Y-%m-%d')
            data_fim = datetime.now().strftime('%Y-%m-%d')
            hoje = datetime.now()
            parcela_all = parcela.objects.filter(data__range=(data_inicio, data_fim)).all().order_by('data')
            if request.method == 'POST' and request.POST.get('parcela_id') != None:
                data_inicio = request.POST.get('data_inicio')
                data_fim = request.POST.get('data_fim')
                parcela_id = request.POST.get('parcela_id')
                parcela_obj = parcela.objects.filter(id=parcela_id).get()  
                data_pagamento = datetime.now()    
                parcela_obj.estado = 2
                parcela_obj.save()
                conta_empresa_obj = conta_empresa.objects.latest('id')
                ultimo_id = parcela_obj.id
                novo_total = conta_empresa_obj.total + parcela_obj.valor
                valor = parcela_obj.valor
                desc = "Recebimento da Parcela : " + str(parcela_obj.id)
                nova_saida = conta_empresa(operacao=1, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                nova_saida.save()
                parcela_all = parcela.objects.filter(data__range=(data_inicio,data_fim)).all().order_by('data')
                return render(request, 'lavajato_contas/conta_receber.html', {'title':'Receber Conta', 'data_inicio':data_inicio, 'data_fim':data_fim, 'parcela_all':parcela_all})
            return render(request, 'lavajato_contas/conta_receber.html', {'title':'Receber Conta', 'data_inicio':data_inicio, 'data_fim':data_fim, 'parcela_all':parcela_all})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def receber(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            data_inicio = datetime.now().strftime('%Y-%m-%d')
            data_fim = datetime.now().strftime('%Y-%m-%d')
            mes = datetime.now().month
            t_receber = 0
            n_receber = 0
            t_recebido = 0
            n_recebido = 0
            n_geral = 0
            parcela_all = parcela.objects.filter(data__month=mes).all().order_by('data')
            for a in parcela.objects.filter(estado=1, data__month=mes).all():
                    t_receber = t_receber + a.valor
                    n_receber = n_receber + 1
            for b in parcela.objects.filter(estado=2, data__month=mes).all():
                    t_recebido = t_recebido + b.valor
                    n_recebido = n_recebido + 1
            n_geral = n_receber + n_recebido
            total_geral = t_receber + t_recebido
            if request.method == 'POST' and request.POST.get('data_inicio') != None and request.POST.get('data_fim') != None:
                data_inicio = request.POST.get('data_inicio')
                data_fim = request.POST.get('data_fim')
                t_receber = 0
                n_receber = 0
                t_recebido = 0
                n_recebido = 0
                n_geral = 0
                parcela_all = parcela.objects.filter(data__range=(data_inicio,data_fim)).all().order_by('data')
                for a in parcela.objects.filter(estado=1, data__range=(data_inicio,data_fim)).all():
                        t_receber = t_receber + a.valor
                        n_receber = n_receber + 1
                for b in parcela.objects.filter(estado=2, data__range=(data_inicio,data_fim)).all():
                        t_recebido = t_recebido + b.valor
                        n_recebido = n_recebido + 1
                n_geral = n_receber + n_recebido
                total_geral = t_receber + t_recebido
                return render(request, 'lavajato_contas/conta_relatorio_receber.html', {'title':'Relatorio Contas a Receber', 'data_inicio':data_inicio, 'data_fim':data_fim, 'parcela_all':parcela_all, 'n_receber':n_receber, 't_receber':t_receber, 'n_recebido':n_recebido, 't_recebido':t_recebido, 'total_geral':total_geral, 'n_geral':n_geral})
            return render(request, 'lavajato_contas/conta_relatorio_receber.html', {'title':'Relatorio Contas a Receber', 'data_inicio':data_inicio, 'data_fim':data_fim, 'parcela_all':parcela_all, 'n_receber':n_receber, 't_receber':t_receber, 'n_recebido':n_recebido, 't_recebido':t_recebido, 'total_geral':total_geral, 'n_geral':n_geral})
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
            contas_all = conta.objects.filter(data_venc__month=mes).all().order_by('data_venc')
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
                contas_all = conta.objects.filter(data_venc__range=(data_inicio,data_fim)).all().order_by('data_venc')
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

def excluir(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            if request.method == 'POST' and request.POST.get('conta_id') != None:
                conta_id = request.POST.get('conta_id')
                conta_obj = conta.objects.get(id=conta_id)
                conta_obj.delete()
                msg = conta_obj.nome + " deletado(a) com sucesso!"
                contas = conta.objects.all().order_by('data_venc')
                return render(request, 'lavajato_contas/conta_busca_edita.html', {'title':'Editar Conta', 'msg':msg, 'contas':contas})
            return render(request, 'lavajato_contas/conta_busca_edita.html', {'title':'Editar Conta'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})