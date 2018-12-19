from django.shortcuts import render
from django.utils import timezone
import datetime
from .models import conta
from lavajato_caixa.models import caixa_geral

# Create your views here.
def lavajato_contas(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            if request.method == 'POST' and request.POST.get('nome') != None:
                nome = request.POST.get('nome')
                valor = request.POST.get('valor')
                data_venc = request.POST.get('data_venc')
                nova_conta = conta(nome=nome, valor=valor, data_venc=data_venc, estado=1)
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
                data_venc = request.POST.get('data_venc')
                estado = request.POST.get('estado')
                conta_obj.nome = nome
                conta_obj.valor = valor
                conta_obj.data_venc = data_venc
                conta_obj.estado = estado
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
                conta_obj.data_pagamento = hoje
                conta_obj.estado = 2
                conta_obj.save()
                caixa = caixa_geral.objects.latest('id')
                ultimo_id = caixa.id_operacao
                ultimo_id = int(ultimo_id) + 1
                novo_total = caixa.total - conta_obj.valor
                valor = conta_obj.valor
                desc = "Pagamento da conta : " + str(conta_obj.nome)
                nova_entrada = caixa_geral(operacao=2, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                nova_entrada.save()
                msg = conta_obj.nome + " pago(a) com sucesso!"
                return render(request, 'lavajato_contas/conta_pagar.html', {'title':'Pagar Conta', 'contas':contas, 'msg':msg})
            return render(request, 'lavajato_contas/conta_pagar.html', {'title':'Pagar Conta', 'contas':contas})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})