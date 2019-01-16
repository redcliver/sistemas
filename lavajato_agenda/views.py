from django.shortcuts import render
from django.utils import timezone
import datetime
from datetime import datetime
from datetime import timedelta, date
from decimal import Decimal
from .models import agenda, servico_item, parcela, pagamento
from lavajato_cliente.models import cliente, carro
from lavajato_controle.models import funcionario, servico
from lavajato_caixa.models import caixa_geral

# Create your views here.
def novo(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            clientes = cliente.objects.all().order_by('nome')
            servicos = servico.objects.all().order_by('nome')
            funcionarios = funcionario.objects.all().order_by('nome')
            cliente_obj = None
            if request.method == 'GET' and request.GET.get('cliente_id') != None:
                cliente_id = request.GET.get('cliente_id')
                cliente_obj = cliente.objects.filter(id=cliente_id).get()
                carros = cliente_obj.carros.all()
                servicos = servico.objects.all().order_by('nome')
                funcionarios = funcionario.objects.all().order_by('nome')
                return render(request, 'lavajato_agenda/agenda_novo.html', {'title':'Novo Agendamento', 'clientes':clientes, 'servicos':servicos, 'funcionarios':funcionarios, 'carros':carros, 'cliente_obj':cliente_obj})
            if request.method == 'POST' and request.POST.get('cliente_id') != None:
                cliente_id = request.POST.get('cliente_id')
                cliente_obj = cliente.objects.filter(id=cliente_id).get()
                servico_id = request.POST.get('servico_id')
                servico_obj = servico.objects.filter(id=servico_id).get()
                funcionario_id = request.POST.get('funcionario_id')
                funcionario_obj = funcionario.objects.filter(id=funcionario_id).get()
                carro_id = request.POST.get('carro_id')
                carro_obj = carro.objects.filter(id=carro_id).get()

                data = request.POST.get('data')
                novo_serv_item = servico_item(serv=servico_obj, func=funcionario_obj)
                novo_serv_item.save()
                novo_agendamento = agenda(cli=cliente_obj,car=carro_obj, data = data, estado=1)
                novo_agendamento.save()
                novo_agendamento.item_servico.add(novo_serv_item)
                novo_agendamento.subtotal = servico_obj.valor
                novo_agendamento.total = servico_obj.valor
                novo_agendamento.save()
                msg = cliente_obj.nome+" agendado com sucesso!"
                clientes = cliente.objects.all().order_by('nome')
                servicos = servico.objects.all().order_by('nome')
                funcionarios = funcionario.objects.all().order_by('nome')
                return render(request, 'lavajato_agenda/agenda_novo.html', {'title':'Novo Agendamento', 'msg':msg, 'clientes':clientes, 'servicos':servicos, 'funcionarios':funcionarios})
            return render(request, 'lavajato_agenda/agenda_novo.html', {'title':'Novo Agendamento', 'clientes':clientes, 'servicos':servicos, 'funcionarios':funcionarios, 'cliente_obj':cliente_obj})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def busca(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = datetime.now().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(estado=1).order_by('data')
            if request.method == 'POST' and request.POST.get('agenda_id') != None:
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                servicos = servico.objects.all().order_by('nome')
                funcionarios = funcionario.objects.all().order_by('nome')
                it_servicos = agenda_obj.item_servico.all()
                return render(request, 'lavajato_agenda/agenda_add_servico.html', {'title':'Adicionar Servico', 'agenda_obj':agenda_obj, 'servicos':servicos, 'funcionarios':funcionarios, 'it_servicos':it_servicos})
            return render(request, 'lavajato_agenda/agenda_busca.html', {'title':'Editar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def add_servico(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            agendas = agenda.objects.filter(estado=1).order_by('data')
            servicos = servico.objects.all().order_by('nome')
            funcionarios = funcionario.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('agenda_id') != None and request.POST.get('servico_id') != None:
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                servico_id = request.POST.get('servico_id')
                servico_obj = servico.objects.filter(id=servico_id).get()
                funcionario_id = request.POST.get('funcionario_id')
                funcionario_obj = funcionario.objects.filter(id=funcionario_id).get()
                novo_serv_item = servico_item(serv=servico_obj, func=funcionario_obj)
                novo_serv_item.save()
                agenda_obj.item_servico.add(novo_serv_item)
                agenda_obj.subtotal = agenda_obj.subtotal + servico_obj.valor
                agenda_obj.total = agenda_obj.total + servico_obj.valor
                agenda_obj.save()
                it_servicos = agenda_obj.item_servico.all()
                msg = agenda_obj.cli.nome+" editado com sucesso!"
                agendas = agenda.objects.filter(estado=1).order_by('data')
                servicos = servico.objects.all().order_by('nome')
                funcionarios = funcionario.objects.all().order_by('nome')
                return render(request, 'lavajato_agenda/agenda_add_servico.html', {'title':'Adicionar Servico ', 'it_servicos':it_servicos, 'msg':msg, 'agenda_obj':agenda_obj, 'servicos':servicos, 'funcionarios':funcionarios})
            return render(request, 'lavajato_agenda/agenda_add_servico.html', {'title':'Adicionar Servico', 'agendas':agendas, 'servicos':servicos, 'funcionarios':funcionarios})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def edita(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = datetime.now().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(data__date=timezone.now()).all()
            if request.method == 'POST' and request.POST.get('data') != None:
                hoje = request.POST.get('data')
                agendas = agenda.objects.filter(data__date=hoje).all()
                return render(request, 'lavajato_agenda/agenda_edita.html', {'title':'Editar Agenda', 'agendas':agendas, 'hoje':hoje})
            if request.method == 'GET' and request.GET.get('agenda_id') != None:
                agenda_id = request.GET.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                it_servicos = agenda_obj.item_servico.all()
                return render(request, 'lavajato_agenda/agenda_edita.1.html', {'title':'Editar Agenda', 'agenda_obj':agenda_obj, 'it_servicos':it_servicos})
            return render(request, 'lavajato_agenda/agenda_edita.html', {'title':'Editar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def excluir(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = datetime.now().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(data__date=hoje)
            if request.method == 'POST' and request.POST.get('servico_item_id') != None and request.POST.get('agenda_id') != None:
                servico_item_id = request.POST.get('servico_item_id')
                servico_item_obj = servico_item.objects.filter(id=servico_item_id).get()
                servico_item_obj.cancelado = 2
                servico_item_obj.serv.valor = servico_item_obj.serv.valor * -1
                servico_item_obj.save()
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                agenda_obj.subtotal = agenda_obj.subtotal + servico_item_obj.serv.valor
                agenda_obj.total = agenda_obj.total + servico_item_obj.serv.valor
                agenda_obj.save()
                it_servicos = agenda_obj.item_servico.all()
                return render(request, 'lavajato_agenda/agenda_edita.1.html', {'title':'Editar Agenda', 'agenda_obj':agenda_obj, 'it_servicos':it_servicos})
            return render(request, 'lavajato_agenda/agenda_edita.html', {'title':'Editar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def visualiza(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = datetime.now().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(data__date=hoje).all()
            if request.method == 'POST' and request.POST.get('data') != None:
                hoje = request.POST.get('data')
                agendas = agenda.objects.filter(data__date=hoje).all()
                return render(request, 'lavajato_agenda/agenda_visualiza.html', {'title':'Visualizar Agenda', 'agendas':agendas, 'hoje':hoje})
            return render(request, 'lavajato_agenda/agenda_visualiza.html', {'title':'Visualizar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def ver(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            agendas = agenda.objects.filter(estado=1).order_by('data')
            servicos = servico.objects.all().order_by('nome')
            funcionarios = funcionario.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('agenda_id') != None:
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                it_servicos = agenda_obj.item_servico.all()
                hoje = datetime.now().strftime('%d/%m/%Y')
                return render(request, 'lavajato_agenda/agenda_ver.html', {'title':'Orcamento', 'agenda_obj':agenda_obj, 'it_servicos':it_servicos, 'hoje':hoje})
            return render(request, 'lavajato_agenda/agenda_ver.html', {'title':'Visualizar Ordem', 'agendas':agendas, 'servicos':servicos, 'funcionarios':funcionarios})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def confirmacao(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = datetime.now().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(data__date=hoje).all()
            if request.method == 'POST' and request.POST.get('agenda_id') != None:
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                desc_total = agenda_obj.subtotal - agenda_obj.desconto
                servicos = agenda_obj.item_servico.all()
                return render(request, 'lavajato_agenda/agenda_confirmacao.html', {'title':'Confirmar Agenda', 'agenda_obj':agenda_obj, 'servicos':servicos, 'desc_total':desc_total})
            return render(request, 'lavajato_agenda/agenda_visualiza.html', {'title':'Visualizar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def desconto(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = datetime.now().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(data__date=hoje).all()
            if request.method == 'POST' and request.POST.get('agenda_id') != None and request.POST.get('desconto') != None:
                agenda_id = request.POST.get('agenda_id')
                desconto = request.POST.get('desconto')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                agenda_obj.desconto = desconto
                desc_total = agenda_obj.total - Decimal(desconto)
                agenda_obj.total = desc_total
                agenda_obj.save()
                servicos = agenda_obj.item_servico.all()
                return render(request, 'lavajato_agenda/agenda_confirmacao.html', {'title':'Confirmar Agenda', 'agenda_obj':agenda_obj, 'servicos':servicos, 'desc_total':desc_total})
            return render(request, 'lavajato_agenda/agenda_visualiza.html', {'title':'Visualizar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def desmarcar(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = datetime.now().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(data__date=hoje)
            if request.method == 'POST' and request.POST.get('agenda_id') != None:
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                agenda_obj.estado = 2
                agenda_obj.save()
                msg = "Agendamento numero "+str(agenda_obj.id)+" desmarcado com sucesso."
                hoje = datetime.now().strftime('%Y-%m-%d')
                agendas = agenda.objects.filter(data__date=hoje)
                return render(request, 'lavajato_agenda/agenda_visualiza.html', {'title':'Desmarcar Agendamento', 'agendas':agendas, 'hoje':hoje, 'agenda_obj':agenda_obj, 'msg':msg})
            return render(request, 'lavajato_agenda/agenda_visualiza.html', {'title':'Visualizar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def dinheiro(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = datetime.now().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(estado=1).order_by('data')
            if request.method == 'GET' and request.GET.get('agenda_id') != None:
                agenda_id = request.GET.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                desc_total = agenda_obj.subtotal - agenda_obj.desconto
                return render(request, 'lavajato_agenda/agenda_troco.html', {'title':'Troco', 'agenda_obj':agenda_obj, 'desc_total':desc_total})
            if request.method == 'POST' and request.POST.get('recebido') != None and request.POST.get('agenda_id') != None:
                agenda_id = request.POST.get('agenda_id')
                recebido = request.POST.get('recebido')
                hoje = datetime.now().strftime('%Y-%m-%d')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                desc_total = agenda_obj.subtotal - agenda_obj.desconto
                agenda_obj.total = desc_total
                agenda_obj.save()
                troco = agenda_obj.total - Decimal(recebido)
                troco= troco * -1
                agenda_obj.estado = 3
                agenda_obj.pagas_parcelas = 1
                agenda_obj.save()
                valor = agenda_obj.total
                novo_pagamento = pagamento(tipo=1,valor=valor)
                novo_pagamento.save()
                agenda_obj.pag.add(novo_pagamento)
                agenda_obj.save()
                nova_parcela = parcela(estado=2, valor=agenda_obj.total, pag ="Dinheiro", data_pagamento=hoje)
                nova_parcela.save()
                agenda_obj.parcelas.add(nova_parcela)
                agenda_obj.save()
                caixa = caixa_geral.objects.latest('id')
                ultimo_id = agenda_obj.id
                novo_total = caixa.total + valor
                desc = "Agendamento N:" + str(agenda_obj.id)
                nova_entrada = caixa_geral(operacao=1, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                nova_entrada.save()
                msg = "Pagamento do agendamento "+str(agenda_obj.id)+ "concluido com sucesso."
                return render(request, 'lavajato_agenda/agenda_troco.1.html', {'title':'Confirmar Agenda', 'agenda_obj':agenda_obj, 'troco':troco, 'recebido':recebido})
            return render(request, 'lavajato_agenda/agenda_visualiza.html', {'title':'Visualizar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def debito(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            if request.method == 'GET' and request.GET.get('agenda_id') != None:
                agenda_id = request.GET.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                return render(request, 'lavajato_agenda/agenda_troco.html', {'title':'Troco', 'agenda_obj':agenda_obj})
            if request.method == 'POST' and request.POST.get('agenda_id') != None:
                data_pag = timezone.now() + timezone.timedelta(days=2)
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                desc_total = agenda_obj.subtotal - agenda_obj.desconto
                agenda_obj.total = desc_total
                agenda_obj.estado = 3
                agenda_obj.pagas_parcelas = 1
                agenda_obj.save()
                valor = agenda_obj.total
                novo_pagamento = pagamento(tipo=2,valor=valor)
                novo_pagamento.save()
                agenda_obj.pag.add(novo_pagamento)
                agenda_obj.save()
                nova_parcela = parcela(estado=1, valor=agenda_obj.total, pag ="Cartao Debito", data=data_pag)
                nova_parcela.save()
                agenda_obj.parcelas.add(nova_parcela)
                agenda_obj.save()
                caixa = caixa_geral.objects.latest('id')
                novo_total = caixa.total + agenda_obj.total
                valor = agenda_obj.total
                desc = "Agendamento N:" + str(agenda_obj.id)
                nova_entrada = caixa_geral(operacao=1, id_operacao=agenda_obj.id, valor_operacao=valor, descricao=desc, total=novo_total)
                nova_entrada.save()
                msg = "Pagamento do agendamento "+str(agenda_obj.id)+ " concluido com sucesso."
                total_msg = "Total: R$"+ str(valor)
                return render(request, 'lavajato_home/home.html', {'title':'Home', 'msg':msg, 'total_msg':total_msg})
            return render(request, 'lavajato_agenda/agenda_visualiza.html', {'title':'Visualizar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def credito(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = datetime.now().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(data__icontains=hoje)
            if request.method == 'POST' and request.POST.get('agenda_id') != None and request.POST.get('n_parcelas') == '1':
                data_pag = timezone.now() + timezone.timedelta(days=30)
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                desc_total = agenda_obj.subtotal - agenda_obj.desconto
                agenda_obj.total = desc_total
                agenda_obj.estado = 3
                agenda_obj.save()
                valor = agenda_obj.total
                novo_pagamento = pagamento(tipo=3,valor=valor)
                novo_pagamento.save()
                agenda_obj.pag.add(novo_pagamento)
                agenda_obj.save()
                nova_parcela = parcela(estado=1, valor=agenda_obj.total, pag ="Cartao Credito", data=data_pag)
                nova_parcela.save()
                agenda_obj.parcelas.add(nova_parcela)
                agenda_obj.save()
                caixa = caixa_geral.objects.latest('id')
                novo_total = caixa.total + agenda_obj.total
                valor = agenda_obj.total
                desc = "Agendamento N:" + str(agenda_obj.id)
                nova_entrada = caixa_geral(operacao=1, id_operacao=agenda_obj.id, valor_operacao=valor, descricao=desc, total=novo_total)
                nova_entrada.save()
                msg = "Pagamento do agendamento "+str(agenda_obj.id)+ " concluido com sucesso."
                return render(request, 'lavajato_home/home.html', {'title':'Home', 'msg':msg})
            if request.method == 'POST' and request.POST.get('agenda_id') != None and request.POST.get('n_parcelas') != '1':
                p = 0
                c = 1
                data_pag = timezone.now() + timezone.timedelta(days=30)
                agenda_id = request.POST.get('agenda_id')
                n_parcelas = request.POST.get('n_parcelas')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                desc_total = agenda_obj.subtotal - agenda_obj.desconto
                agenda_obj.total = desc_total
                agenda_obj.total_parcelas = int(n_parcelas)
                agenda_obj.estado = 3
                agenda_obj.save()
                valor = agenda_obj.total
                v_parcela = valor / int(n_parcelas)
                while p < int(n_parcelas):
                    data_parcela = timedelta(days=30) * c
                    data_pag = datetime.now() + data_parcela
                    nova_parcela = parcela(estado=1, valor=v_parcela, numero_parcela=c, total_parcelas=int(n_parcelas), pag ="Cartao Credito", data=data_pag)
                    nova_parcela.save()
                    agenda_obj.parcelas.add(nova_parcela)
                    agenda_obj.save()
                    p = p + 1
                    c = c + 1
                novo_pagamento = pagamento(tipo=3,valor=valor)
                novo_pagamento.save()
                agenda_obj.pag.add(novo_pagamento)
                agenda_obj.save()
                caixa = caixa_geral.objects.latest('id')
                novo_total = caixa.total + agenda_obj.total
                valor = agenda_obj.total
                desc = "Agendamento N:" + str(agenda_obj.id)
                nova_entrada = caixa_geral(operacao=1, id_operacao=agenda_obj.id, valor_operacao=valor, descricao=desc, total=novo_total)
                nova_entrada.save()
                msg = "Pagamento do agendamento "+str(agenda_obj.id)+ " concluido com sucesso."
                return render(request, 'lavajato_home/home.html', {'title':'Home', 'msg':msg})
            
            return render(request, 'lavajato_agenda/agenda_visualiza.html', {'title':'Visualizar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def metodo2(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = datetime.now().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(estado=1).order_by('data')
            if request.method == 'POST' and request.POST.get('dinheiro') != None and request.POST.get('agenda_id') != None and request.POST.get('cartao') != None:
                p = 0
                c = 1
                agenda_id = request.POST.get('agenda_id')
                dinheiro = request.POST.get('dinheiro')
                cartao = request.POST.get('cartao')
                n_parcelas = request.POST.get('n_parcelas')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                desc_total = agenda_obj.subtotal - agenda_obj.desconto
                agenda_obj.total = desc_total
                agenda_obj.save()
                agenda_obj.estado = 3
                agenda_obj.pagas_parcelas = 1
                agenda_obj.save()
                valor_1 = agenda_obj.total
                valor = agenda_obj.total - Decimal(dinheiro)
                novo_pagamento = pagamento(tipo=1,valor=Decimal(dinheiro), pag="Dinheiro")
                novo_pagamento.save()
                agenda_obj.pag.add(novo_pagamento)
                agenda_obj.save()
                v_parcela = valor / int(n_parcelas)
                while p < int(n_parcelas):
                    data_parcela = timedelta(days=30) * c
                    data_pag = datetime.now() + data_parcela
                    nova_parcela = parcela(estado=1, valor=v_parcela, numero_parcela=c, total_parcelas=int(n_parcelas), pag="Cartao Credito", data=data_pag)
                    nova_parcela.save()
                    agenda_obj.parcelas.add(nova_parcela)
                    agenda_obj.save()
                    p = p + 1
                    c = c + 1
                novo_pagamento1 = pagamento(tipo=3,valor=valor)
                novo_pagamento1.save()
                agenda_obj.pag.add(novo_pagamento1)
                agenda_obj.save()
                caixa = caixa_geral.objects.latest('id')
                ultimo_id = agenda_obj.id
                novo_total = caixa.total + valor_1
                desc = "Agendamento N:" + str(agenda_obj.id)
                nova_entrada = caixa_geral(operacao=1, id_operacao=ultimo_id, valor_operacao=valor_1, descricao=desc, total=novo_total)
                nova_entrada.save()
                msg = "Pagamento do agendamento "+str(agenda_obj.id)+ "concluido com sucesso."
                return render(request, 'lavajato_home/home.html', {'title':'Home', 'msg':msg})
            return render(request, 'lavajato_agenda/agenda_visualiza.html', {'title':'Visualizar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})