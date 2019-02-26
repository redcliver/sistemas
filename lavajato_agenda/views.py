from django.shortcuts import render
from django.utils import timezone
import datetime
from datetime import datetime
from datetime import timedelta, date
from django.utils.dateparse import parse_date
from decimal import Decimal
from .models import agenda, servico_item, parcela, pagamento
from lavajato_cliente.models import cliente, carro
from lavajato_controle.models import funcionario, servico, taxa
from lavajato_caixa.models import caixa_geral

# Create your views here.
def novo(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            clientes = cliente.objects.filter(liberacao=1).all().order_by('nome')
            servicos = servico.objects.all().order_by('nome')
            funcionarios = funcionario.objects.all().order_by('nome')
            cliente_obj = None
            if request.method == 'GET' and request.GET.get('cliente_id') != None:
                hoje = datetime.now().strftime('%Y-%m-%d')
                cliente_id = request.GET.get('cliente_id')
                cliente_obj = cliente.objects.filter(id=cliente_id).get()
                carros = cliente_obj.carros.all()
                servicos = servico.objects.all().order_by('nome')
                funcionarios = funcionario.objects.all().order_by('nome')
                return render(request, 'lavajato_agenda/agenda_novo.html', {'title':'Novo Agendamento', 'clientes':clientes, 'servicos':servicos, 'funcionarios':funcionarios, 'carros':carros, 'cliente_obj':cliente_obj, 'hoje':hoje})
            if request.method == 'POST' and request.POST.get('cliente_id') != None:
                cliente_id = request.POST.get('cliente_id')
                cliente_obj = cliente.objects.filter(id=cliente_id).get()
                servico_id = request.POST.get('servico_id')
                servico_obj = servico.objects.filter(id=servico_id).get()
                funcionario_id = request.POST.get('funcionario_id')
                funcionario_obj = funcionario.objects.filter(id=funcionario_id).get()
                carro_id = request.POST.get('carro_id')
                carro_obj = carro.objects.filter(id=carro_id).get()
                obs = request.POST.get('obs')
                data = request.POST.get('data')
                data_pagamento = request.POST.get('data_pagamento')
                novo_serv_item = servico_item(serv=servico_obj, func=funcionario_obj)
                novo_serv_item.save()
                novo_agendamento = agenda(cli=cliente_obj,car=carro_obj, data = data, estado=1, obs=obs, data_pagamento=data_pagamento)
                novo_agendamento.save()
                novo_agendamento.item_servico.add(novo_serv_item)
                novo_agendamento.subtotal = servico_obj.valor
                novo_agendamento.total = servico_obj.valor
                novo_agendamento.save()
                msg = cliente_obj.nome+" agendado com sucesso!"
                clientes = cliente.objects.all().order_by('nome')
                servicos = servico.objects.all().order_by('nome')
                funcionarios = funcionario.objects.all().order_by('nome')
                it_servicos = novo_agendamento.item_servico.all()
                return render(request, 'lavajato_agenda/agenda_add_servico.html', {'title':'Novo Servico', 'agenda_obj':novo_agendamento, 'it_servicos':it_servicos, 'msg':msg, 'clientes':clientes, 'servicos':servicos, 'funcionarios':funcionarios})
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

def salvar(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            if request.method == 'POST' and request.POST.get('obs') != None and request.POST.get('agenda_id') != None:
                obs = request.POST.get('obs')
                agenda_id = request.POST.get('agenda_id')
                data_pagamento = request.POST.get('data_pagamento')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                agenda_obj.data_pagamento = data_pagamento
                agenda_obj.obs = obs
                agenda_obj.save()
                msg = "Ordem alterada com sucesso"
                it_servicos = agenda_obj.item_servico.all()
                hoje = datetime.now().strftime('%Y-%m-%d')
                agendas = agenda.objects.filter(data__date=timezone.now()).all()
                return render(request, 'lavajato_agenda/agenda_edita.html', {'title':'Editar Agenda', 'agendas':agendas, 'hoje':hoje})
            return render(request, 'lavajato_agenda/agenda_visualiza.html', {'title':'Salva Agenda'})
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
            agendas = agenda.objects.filter(data__date=hoje).all().order_by('estado')
            if request.method == 'POST' and request.POST.get('data') != None:
                hoje = request.POST.get('data')
                agendas = agenda.objects.filter(data__date=hoje).all().order_by('estado')
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

def checklist(request):
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
                return render(request, 'lavajato_agenda/agenda_checklist.html', {'title':'Check-list', 'agenda_obj':agenda_obj, 'it_servicos':it_servicos, 'hoje':hoje})
            return render(request, 'lavajato_agenda/agenda_checklist.html', {'title':'Check-list', 'agendas':agendas, 'servicos':servicos, 'funcionarios':funcionarios})
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
                servicos = agenda_obj.item_servico.all()
                return render(request, 'lavajato_agenda/agenda_confirmacao.html', {'title':'Confirmar Agenda', 'agenda_obj':agenda_obj, 'servicos':servicos})
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
                agenda_obj.desconto = agenda_obj.desconto + Decimal(desconto)
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
            if request.method == 'POST' and request.POST.get('agenda_id') != None and request.POST.get('dinheiro') != None:
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                servicos = agenda_obj.item_servico.all()
                dinheiro = request.POST.get('dinheiro')
                dinheiro = Decimal(dinheiro)
                if agenda_obj.total < dinheiro:
                    servicos = agenda_obj.item_servico.all()
                    msg = "Pagamento de R$"+str(dinheiro)+ " é maior que o valor total."
                    return render(request, 'lavajato_agenda/agenda_confirmacao.html', {'title':'Confirmar Agenda', 'agenda_obj':agenda_obj, 'servicos':servicos, 'msg':msg})
                elif dinheiro == agenda_obj.total:
                    hoje = timezone.now()
                    agenda_obj.estado = 3
                    agenda_obj.pagas_parcelas = agenda_obj.pagas_parcelas + 1
                    agenda_obj.save()
                    valor = agenda_obj.total
                    novo_pagamento = pagamento(tipo=1,valor=dinheiro)
                    novo_pagamento.save()
                    agenda_obj.pag.add(novo_pagamento)
                    agenda_obj.save()
                    nova_parcela = parcela(estado=2, valor=dinheiro, pag = 1, data_pagamento=hoje)
                    nova_parcela.save()
                    agenda_obj.parcelas.add(nova_parcela)
                    agenda_obj.pag_parcial = agenda_obj.pag_parcial + dinheiro
                    agenda_obj.save()
                    caixa = caixa_geral.objects.latest('id')
                    id_op = agenda_obj.id
                    novo_total = caixa.total + dinheiro
                    desc = "OS N:" + str(agenda_obj.id)
                    nova_entrada = caixa_geral(operacao=1, tipo=1, id_operacao=id_op, valor_operacao=dinheiro, descricao=desc, total=novo_total)
                    nova_entrada.save()
                    msg = "Pagamento do agendamento "+str(agenda_obj.id)+ " concluído com sucesso."
                    return render(request, 'lavajato_home/home.html', {'title':'Home', 'msg':msg})
                elif dinheiro < agenda_obj.total:
                    hoje = timezone.now()
                    agenda_obj.estado = 1
                    agenda_obj.pagas_parcelas = agenda_obj.pagas_parcelas + 1
                    agenda_obj.save()
                    novo_pagamento = pagamento(tipo=1,valor=dinheiro)
                    novo_pagamento.save()
                    agenda_obj.pag.add(novo_pagamento)
                    agenda_obj.save()
                    nova_parcela = parcela(estado=2, valor=dinheiro, pag = 1, data_pagamento=hoje)
                    nova_parcela.save()
                    agenda_obj.parcelas.add(nova_parcela)
                    agenda_obj.total = agenda_obj.total - dinheiro
                    agenda_obj.pag_parcial = agenda_obj.pag_parcial + dinheiro
                    agenda_obj.save()
                    caixa = caixa_geral.objects.latest('id')
                    id_op = agenda_obj.id
                    novo_total = caixa.total + dinheiro
                    desc = "OS N:" + str(agenda_obj.id) 
                    nova_entrada = caixa_geral(operacao=1, tipo=1, id_operacao=id_op, valor_operacao=dinheiro, descricao=desc, total=novo_total)
                    nova_entrada.save()
                    servicos = agenda_obj.item_servico.all()
                    msg = "Pagamento de R$"+str(dinheiro)+ " foi registrado no sistema."
                    return render(request, 'lavajato_agenda/agenda_confirmacao.html', {'title':'Confirmar Agenda', 'agenda_obj':agenda_obj, 'servicos':servicos, 'msg':msg})      
            return render(request, 'lavajato_agenda/agenda_confirmacao.html', {'title':'Confirmar Agenda'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def elo_debito(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            if request.method == 'POST' and request.POST.get('agenda_id') != None and request.POST.get('debito') != None:
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                servicos = agenda_obj.item_servico.all()
                debito = request.POST.get('debito')
                debito = Decimal(debito)
                if agenda_obj.total < debito:
                    servicos = agenda_obj.item_servico.all()
                    msg = "Pagamento de R$"+str(debito)+ " é maior que o valor total."
                    return render(request, 'lavajato_agenda/agenda_confirmacao.html', {'title':'Confirmar Agenda', 'agenda_obj':agenda_obj, 'servicos':servicos, 'msg':msg})
                elif debito == agenda_obj.total:
                    hoje = timezone.now()
                    taxas = taxa.objects.get(tipo=4)
                    dia = taxas.dias
                    data_pag = timezone.now() + timezone.timedelta(days=int(dia))
                    novo_pagamento = pagamento(tipo=4,valor=debito)
                    novo_pagamento.save()
                    agenda_obj.pag.add(novo_pagamento)
                    agenda_obj.save()
                    v_juros = debito / 100
                    t_juros = float(v_juros) * float(taxas.juros)
                    val_parc = float(debito) - float(t_juros)
                    nova_parcela = parcela(estado=1, valor=val_parc, pag = 4, data=data_pag)
                    nova_parcela.save()
                    agenda_obj.parcelas.add(nova_parcela)
                    agenda_obj.pagas_parcelas = agenda_obj.pagas_parcelas + 1
                    agenda_obj.estado = 3
                    agenda_obj.pag_parcial = agenda_obj.pag_parcial + debito
                    agenda_obj.save()
                    caixa = caixa_geral.objects.latest('id')
                    novo_total = caixa.total + debito
                    desc = "OS N:" + str(agenda_obj.id) 
                    nova_entrada = caixa_geral(operacao=1, tipo=4, id_operacao=agenda_obj.id, valor_operacao=debito, descricao=desc, total=novo_total)
                    nova_entrada.save()
                    msg = "Pagamento do agendamento " +str(agenda_obj.id)+ " concluído com sucesso."
                    return render(request, 'lavajato_home/home.html', {'title':'Home', 'msg':msg})
                elif debito < agenda_obj.total:
                    hoje = timezone.now()
                    taxas = taxa.objects.get(tipo=4)
                    dia = taxas.dias
                    data_pag = timezone.now() + timezone.timedelta(days=int(dia))
                    novo_pagamento = pagamento(tipo=4,valor=debito)
                    novo_pagamento.save()
                    agenda_obj.pag.add(novo_pagamento)
                    agenda_obj.save()
                    v_juros = debito / 100
                    t_juros = float(v_juros) * float(taxas.juros)
                    val_parc = float(debito) - float(t_juros)
                    nova_parcela = parcela(estado=1, valor=val_parc, pag = 4, data=data_pag)
                    nova_parcela.save()
                    agenda_obj.parcelas.add(nova_parcela)
                    agenda_obj.pagas_parcelas = agenda_obj.pagas_parcelas + 1
                    agenda_obj.pag_parcial = agenda_obj.pag_parcial + debito
                    agenda_obj.total = agenda_obj.total - debito
                    agenda_obj.save()
                    caixa = caixa_geral.objects.latest('id')
                    novo_total = caixa.total + debito
                    desc = "Agendamento N:" + str(agenda_obj.id)
                    nova_entrada = caixa_geral(operacao=1, tipo=4, id_operacao=agenda_obj.id, valor_operacao=debito, descricao=desc, total=novo_total)
                    nova_entrada.save()
                    servicos = agenda_obj.item_servico.all()
                    msg = "Pagamento de R$"+str(debito)+ " foi registrado no sistema."
                    return render(request, 'lavajato_agenda/agenda_confirmacao.html', {'title':'Confirmar Agenda', 'agenda_obj':agenda_obj, 'servicos':servicos, 'msg':msg})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})   

def debito(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            if request.method == 'POST' and request.POST.get('agenda_id') != None and request.POST.get('debito') != None:
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                servicos = agenda_obj.item_servico.all()
                debito = request.POST.get('debito')
                debito = Decimal(debito)
                if agenda_obj.total < debito:
                    servicos = agenda_obj.item_servico.all()
                    msg = "Pagamento de R$"+str(debito)+ " é maior que o valor total."
                    return render(request, 'lavajato_agenda/agenda_confirmacao.html', {'title':'Confirmar Agenda', 'agenda_obj':agenda_obj, 'servicos':servicos, 'msg':msg})
                elif debito == agenda_obj.total:
                    hoje = timezone.now()
                    taxas = taxa.objects.get(tipo=3)
                    dia = taxas.dias
                    data_pag = timezone.now() + timezone.timedelta(days=int(dia))
                    novo_pagamento = pagamento(tipo=3,valor=debito)
                    novo_pagamento.save()
                    agenda_obj.pag.add(novo_pagamento)
                    agenda_obj.save()
                    v_juros = debito / 100
                    t_juros = float(v_juros) * float(taxas.juros)
                    val_parc = float(debito) - float(t_juros)
                    nova_parcela = parcela(estado=1, valor=val_parc, pag = 3, data=data_pag)
                    nova_parcela.save()
                    agenda_obj.parcelas.add(nova_parcela)
                    agenda_obj.pagas_parcelas = agenda_obj.pagas_parcelas + 1
                    agenda_obj.estado = 3
                    agenda_obj.pag_parcial = agenda_obj.pag_parcial + debito
                    agenda_obj.save()
                    caixa = caixa_geral.objects.latest('id')
                    novo_total = caixa.total + debito
                    desc = "OS N:" + str(agenda_obj.id) 
                    nova_entrada = caixa_geral(operacao=1, tipo=3, id_operacao=agenda_obj.id, valor_operacao=debito, descricao=desc, total=novo_total)
                    nova_entrada.save()
                    msg = "Pagamento do agendamento " +str(agenda_obj.id)+ " concluído com sucesso."
                    return render(request, 'lavajato_home/home.html', {'title':'Home', 'msg':msg})
                elif debito < agenda_obj.total:
                    hoje = timezone.now()
                    taxas = taxa.objects.get(tipo=3)
                    dia = taxas.dias
                    data_pag = timezone.now() + timezone.timedelta(days=int(dia))
                    novo_pagamento = pagamento(tipo=3,valor=debito)
                    novo_pagamento.save()
                    agenda_obj.pag.add(novo_pagamento)
                    agenda_obj.save()
                    v_juros = debito / 100
                    t_juros = float(v_juros) * float(taxas.juros)
                    val_parc = float(debito) - float(t_juros)
                    nova_parcela = parcela(estado=1, valor=val_parc, pag = 3, data=data_pag)
                    nova_parcela.save()
                    agenda_obj.parcelas.add(nova_parcela)
                    agenda_obj.pagas_parcelas = agenda_obj.pagas_parcelas + 1
                    agenda_obj.pag_parcial = agenda_obj.pag_parcial + debito
                    agenda_obj.total = agenda_obj.total - debito
                    agenda_obj.save()
                    caixa = caixa_geral.objects.latest('id')
                    novo_total = caixa.total + debito
                    desc = "Agendamento N:" + str(agenda_obj.id) 
                    nova_entrada = caixa_geral(operacao=1, tipo=3, id_operacao=agenda_obj.id, valor_operacao=debito, descricao=desc, total=novo_total)
                    nova_entrada.save()
                    servicos = agenda_obj.item_servico.all()
                    msg = "Pagamento de R$"+str(debito)+ " foi registrado no sistema."
                    return render(request, 'lavajato_agenda/agenda_confirmacao.html', {'title':'Confirmar Agenda', 'agenda_obj':agenda_obj, 'servicos':servicos, 'msg':msg})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})   

def elo_credito(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            if request.method == 'POST' and request.POST.get('agenda_id') != None and request.POST.get('credito') != None:
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                servicos = agenda_obj.item_servico.all()
                credito = request.POST.get('credito')
                credito = Decimal(credito)
                if agenda_obj.total < credito:
                    servicos = agenda_obj.item_servico.all()
                    msg = "Pagamento de R$"+str(credito)+ " é maior que o valor total."
                    return render(request, 'lavajato_agenda/agenda_confirmacao.html', {'title':'Confirmar Agenda', 'agenda_obj':agenda_obj, 'servicos':servicos, 'msg':msg})
                elif credito == agenda_obj.total and request.POST.get('n_parcelas') == '1':
                    hoje = timezone.now()
                    taxas = taxa.objects.get(tipo=5)
                    dia = taxas.dias
                    data_pag = timezone.now() + timezone.timedelta(days=int(dia))
                    novo_pagamento = pagamento(tipo=5,valor=credito)
                    novo_pagamento.save()
                    agenda_obj.pag.add(novo_pagamento)
                    agenda_obj.save()
                    v_juros = credito / 100
                    t_juros = float(v_juros) * float(taxas.juros)
                    val_parc = float(credito) - float(t_juros)
                    nova_parcela = parcela(estado=1, valor=val_parc, pag = 5, data=data_pag)
                    nova_parcela.save()
                    agenda_obj.parcelas.add(nova_parcela)
                    agenda_obj.estado = 3
                    agenda_obj.pag_parcial = agenda_obj.pag_parcial + credito
                    agenda_obj.save()
                    caixa = caixa_geral.objects.latest('id')
                    novo_total = caixa.total + credito
                    desc = "OS N:" + str(agenda_obj.id) 
                    nova_entrada = caixa_geral(operacao=1, tipo=5, id_operacao=agenda_obj.id, valor_operacao=credito, descricao=desc, total=novo_total)
                    nova_entrada.save()
                    msg = "Pagamento do agendamento " +str(agenda_obj.id)+ " concluído com sucesso."
                    return render(request, 'lavajato_home/home.html', {'title':'Home', 'msg':msg})
                elif credito == agenda_obj.total and request.POST.get('n_parcelas') != '1':
                    p = 0
                    c = 1
                    hoje = timezone.now()
                    n_parcelas = request.POST.get('n_parcelas')
                    taxas = taxa.objects.get(tipo=5)
                    dia = taxas.dias
                    data_pag = timezone.now() + timezone.timedelta(days=int(dia))
                    v_juros = credito / 100
                    t_juros = float(v_juros) * float(taxas.juros)
                    val_parc = float(credito) - float(t_juros)
                    v_parcela = val_parc / int(n_parcelas)
                    while p < int(n_parcelas):
                        data_parcela = timedelta(days=int(dia)) * c
                        data_pag = datetime.now() + data_parcela
                        nova_parcela = parcela(estado=1, valor=v_parcela, numero_parcela=c, total_parcelas=int(n_parcelas), pag = 5, data=data_pag)
                        nova_parcela.save()
                        agenda_obj.parcelas.add(nova_parcela)
                        agenda_obj.save()
                        p = p + 1
                        c = c + 1
                    novo_pagamento = pagamento(tipo=5,valor=credito)
                    novo_pagamento.save()
                    agenda_obj.pag.add(novo_pagamento)
                    agenda_obj.pag_parcial = agenda_obj.pag_parcial + credito
                    agenda_obj.total = agenda_obj.total - credito
                    agenda_obj.save()
                    caixa = caixa_geral.objects.latest('id')
                    novo_total = caixa.total + credito
                    desc = "OS N:" + str(agenda_obj.id) 
                    nova_entrada = caixa_geral(operacao=1, tipo=5, id_operacao=agenda_obj.id, valor_operacao=credito, descricao=desc, total=novo_total)
                    nova_entrada.save()
                    msg = "Pagamento do agendamento " +str(agenda_obj.id)+ " concluído com sucesso."
                    return render(request, 'lavajato_home/home.html', {'title':'Home', 'msg':msg})
                elif credito < agenda_obj.total and request.POST.get('n_parcelas') == '1':
                    hoje = timezone.now()
                    taxas = taxa.objects.get(tipo=5)
                    dia = taxas.dias
                    data_pag = timezone.now() + timezone.timedelta(days=int(dia))
                    novo_pagamento = pagamento(tipo=5,valor=credito)
                    novo_pagamento.save()
                    agenda_obj.pag.add(novo_pagamento)
                    agenda_obj.save()
                    v_juros = credito / 100
                    t_juros = float(v_juros) * float(taxas.juros)
                    val_parc = float(credito) - float(t_juros)
                    nova_parcela = parcela(estado=1, valor=val_parc, pag = 5, data=data_pag)
                    nova_parcela.save()
                    agenda_obj.parcelas.add(nova_parcela)
                    agenda_obj.pag_parcial = agenda_obj.pag_parcial + credito
                    agenda_obj.total = agenda_obj.total - credito
                    agenda_obj.save()
                    caixa = caixa_geral.objects.latest('id')
                    novo_total = caixa.total + credito
                    desc = "OS N:" + str(agenda_obj.id) 
                    nova_entrada = caixa_geral(operacao=1, tipo=5, id_operacao=agenda_obj.id, valor_operacao=credito, descricao=desc, total=novo_total)
                    nova_entrada.save()
                    servicos = agenda_obj.item_servico.all()
                    msg = "Pagamento de R$"+str(credito)+ " em 1 vez foi registrado no sistema."
                    return render(request, 'lavajato_agenda/agenda_confirmacao.html', {'title':'Confirmar Agenda', 'agenda_obj':agenda_obj, 'servicos':servicos, 'msg':msg})
                elif credito < agenda_obj.total and request.POST.get('n_parcelas') != '1':
                    p = 0
                    c = 1
                    hoje = timezone.now()
                    n_parcelas = request.POST.get('n_parcelas')
                    taxas = taxa.objects.get(tipo=5)
                    dia = taxas.dias
                    data_pag = timezone.now() + timezone.timedelta(days=int(dia))
                    v_juros = credito / 100
                    t_juros = float(v_juros) * float(taxas.juros)
                    val_parc = float(credito) - float(t_juros)
                    v_parcela = val_parc / int(n_parcelas)
                    while p < int(n_parcelas):
                        data_parcela = timedelta(days=int(dia)) * c
                        data_pag = datetime.now() + data_parcela
                        nova_parcela = parcela(estado=1, valor=v_parcela, numero_parcela=c, total_parcelas=int(n_parcelas), pag = 5, data=data_pag)
                        nova_parcela.save()
                        agenda_obj.parcelas.add(nova_parcela)
                        agenda_obj.save()
                        p = p + 1
                        c = c + 1
                    novo_pagamento = pagamento(tipo=5,valor=credito)
                    novo_pagamento.save()
                    agenda_obj.pag.add(novo_pagamento)
                    agenda_obj.pag_parcial = agenda_obj.pag_parcial + credito
                    agenda_obj.total = agenda_obj.total - credito
                    agenda_obj.save()
                    caixa = caixa_geral.objects.latest('id')
                    novo_total = caixa.total + credito
                    desc = "OS N:" + str(agenda_obj.id) 
                    nova_entrada = caixa_geral(operacao=1, tipo=5, id_operacao=agenda_obj.id, valor_operacao=credito, descricao=desc, total=novo_total)
                    nova_entrada.save()
                    servicos = agenda_obj.item_servico.all()
                    msg = "Pagamento de R$"+str(credito)+ " em "+str(n_parcelas)+" vez foi registrado no sistema."
                    return render(request, 'lavajato_agenda/agenda_confirmacao.html', {'title':'Confirmar Agenda', 'agenda_obj':agenda_obj, 'servicos':servicos, 'msg':msg})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'}) 

def credito(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            if request.method == 'POST' and request.POST.get('agenda_id') != None and request.POST.get('credito') != None:
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                servicos = agenda_obj.item_servico.all()
                credito = request.POST.get('credito')
                credito = Decimal(credito)
                if agenda_obj.total < credito:
                    servicos = agenda_obj.item_servico.all()
                    msg = "Pagamento de R$"+str(credito)+ " é maior que o valor total."
                    return render(request, 'lavajato_agenda/agenda_confirmacao.html', {'title':'Confirmar Agenda', 'agenda_obj':agenda_obj, 'servicos':servicos, 'msg':msg})
                elif credito == agenda_obj.total and request.POST.get('n_parcelas') == '1':
                    hoje = timezone.now()
                    taxas = taxa.objects.get(tipo=3)
                    dia = taxas.dias
                    data_pag = timezone.now() + timezone.timedelta(days=int(dia))
                    novo_pagamento = pagamento(tipo=3,valor=credito)
                    novo_pagamento.save()
                    agenda_obj.pag.add(novo_pagamento)
                    agenda_obj.save()
                    v_juros = credito / 100
                    t_juros = float(v_juros) * float(taxas.juros)
                    val_parc = float(credito) - float(t_juros)
                    nova_parcela = parcela(estado=1, valor=val_parc, pag = 3, data=data_pag)
                    nova_parcela.save()
                    agenda_obj.parcelas.add(nova_parcela)
                    agenda_obj.estado = 3
                    agenda_obj.pag_parcial = agenda_obj.pag_parcial + credito
                    agenda_obj.save()
                    caixa = caixa_geral.objects.latest('id')
                    novo_total = caixa.total + credito
                    desc = "OS N:" + str(agenda_obj.id)
                    nova_entrada = caixa_geral(operacao=1, tipo=3, id_operacao=agenda_obj.id, valor_operacao=credito, descricao=desc, total=novo_total)
                    nova_entrada.save()
                    msg = "Pagamento do agendamento " +str(agenda_obj.id)+ " concluído com sucesso."
                    return render(request, 'lavajato_home/home.html', {'title':'Home', 'msg':msg})
                elif credito == agenda_obj.total and request.POST.get('n_parcelas') != '1':
                    p = 0
                    c = 1
                    hoje = timezone.now()
                    n_parcelas = request.POST.get('n_parcelas')
                    taxas = taxa.objects.get(tipo=3)
                    dia = taxas.dias
                    data_pag = timezone.now() + timezone.timedelta(days=int(dia))
                    v_juros = credito / 100
                    t_juros = float(v_juros) * float(taxas.juros)
                    val_parc = float(credito) - float(t_juros)
                    v_parcela = val_parc / int(n_parcelas)
                    while p < int(n_parcelas):
                        data_parcela = timedelta(days=int(dia)) * c
                        data_pag = datetime.now() + data_parcela
                        nova_parcela = parcela(estado=1, valor=v_parcela, numero_parcela=c, total_parcelas=int(n_parcelas), pag = 5, data=data_pag)
                        nova_parcela.save()
                        agenda_obj.parcelas.add(nova_parcela)
                        agenda_obj.save()
                        p = p + 1
                        c = c + 1
                    novo_pagamento = pagamento(tipo=3,valor=credito)
                    novo_pagamento.save()
                    agenda_obj.pag.add(novo_pagamento)
                    agenda_obj.pag_parcial = agenda_obj.pag_parcial + credito
                    agenda_obj.total = agenda_obj.total - credito
                    agenda_obj.estado = 3
                    agenda_obj.save()
                    caixa = caixa_geral.objects.latest('id')
                    novo_total = caixa.total + credito
                    desc = "OS N:" + str(agenda_obj.id) 
                    nova_entrada = caixa_geral(operacao=1, tipo=3, id_operacao=agenda_obj.id, valor_operacao=credito, descricao=desc, total=novo_total)
                    nova_entrada.save()
                    msg = "Pagamento do agendamento " +str(agenda_obj.id)+ " concluído com sucesso."
                    return render(request, 'lavajato_home/home.html', {'title':'Home', 'msg':msg})
                elif credito < agenda_obj.total and request.POST.get('n_parcelas') == '1':
                    hoje = timezone.now()
                    taxas = taxa.objects.get(tipo=3)
                    dia = taxas.dias
                    data_pag = timezone.now() + timezone.timedelta(days=int(dia))
                    novo_pagamento = pagamento(tipo=3,valor=credito)
                    novo_pagamento.save()
                    agenda_obj.pag.add(novo_pagamento)
                    agenda_obj.save()
                    v_juros = credito / 100
                    t_juros = float(v_juros) * float(taxas.juros)
                    val_parc = float(credito) - float(t_juros)
                    nova_parcela = parcela(estado=1, valor=val_parc, pag = 3, data=data_pag)
                    nova_parcela.save()
                    agenda_obj.parcelas.add(nova_parcela)
                    agenda_obj.pag_parcial = agenda_obj.pag_parcial + credito
                    agenda_obj.total = agenda_obj.total - credito
                    agenda_obj.save()
                    caixa = caixa_geral.objects.latest('id')
                    novo_total = caixa.total + credito
                    desc = "OS N:" + str(agenda_obj.id) + " - CRÉDITO"
                    nova_entrada = caixa_geral(operacao=1, tipo=3, id_operacao=agenda_obj.id, valor_operacao=credito, descricao=desc, total=novo_total)
                    nova_entrada.save()
                    servicos = agenda_obj.item_servico.all()
                    msg = "Pagamento de R$"+str(credito)+ " em 1 vez foi registrado no sistema."
                    return render(request, 'lavajato_agenda/agenda_confirmacao.html', {'title':'Confirmar Agenda', 'agenda_obj':agenda_obj, 'servicos':servicos, 'msg':msg})
                elif credito < agenda_obj.total and request.POST.get('n_parcelas') != '1':
                    p = 0
                    c = 1
                    hoje = timezone.now()
                    n_parcelas = request.POST.get('n_parcelas')
                    taxas = taxa.objects.get(tipo=3)
                    dia = taxas.dias
                    data_pag = timezone.now() + timezone.timedelta(days=int(dia))
                    v_juros = credito / 100
                    t_juros = float(v_juros) * float(taxas.juros)
                    val_parc = float(credito) - float(t_juros)
                    v_parcela = val_parc / int(n_parcelas)
                    while p < int(n_parcelas):
                        data_parcela = timedelta(days=int(dia)) * c
                        data_pag = datetime.now() + data_parcela
                        nova_parcela = parcela(estado=1, valor=v_parcela, numero_parcela=c, total_parcelas=int(n_parcelas), pag = 5, data=data_pag)
                        nova_parcela.save()
                        agenda_obj.parcelas.add(nova_parcela)
                        agenda_obj.save()
                        p = p + 1
                        c = c + 1
                    novo_pagamento = pagamento(tipo=3,valor=credito)
                    novo_pagamento.save()
                    agenda_obj.pag.add(novo_pagamento)
                    agenda_obj.pag_parcial = agenda_obj.pag_parcial + credito
                    agenda_obj.total = agenda_obj.total - credito
                    agenda_obj.save()
                    caixa = caixa_geral.objects.latest('id')
                    novo_total = caixa.total + credito
                    desc = "OS N:" + str(agenda_obj.id) 
                    nova_entrada = caixa_geral(operacao=1, tipo=3, id_operacao=agenda_obj.id, valor_operacao=credito, descricao=desc, total=novo_total)
                    nova_entrada.save()
                    servicos = agenda_obj.item_servico.all()
                    msg = "Pagamento de R$"+str(credito)+ " em "+str(n_parcelas)+" vez foi registrado no sistema."
                    return render(request, 'lavajato_agenda/agenda_confirmacao.html', {'title':'Confirmar Agenda', 'agenda_obj':agenda_obj, 'servicos':servicos, 'msg':msg})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'}) 

def boleto(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = datetime.now().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(boleto__lte=hoje, estado=1).all().order_by('boleto')
            if request.method == 'POST' and request.POST.get('data') != None:
                hoje = request.POST.get('data')
                agendas = agenda.objects.filter(data__date=hoje).all().order_by('estado')
                return render(request, 'lavajato_agenda/agenda_boletos.html', {'title':'Boletos em aberto', 'agendas':agendas, 'hoje':hoje})
            return render(request, 'lavajato_agenda/agenda_boletos.html', {'title':'Boletos em aberto', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def add_prazo(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            if request.method == 'GET':
                hoje = datetime.now().strftime('%Y-%m-%d')
                agenda_id = request.GET.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                it_servicos = agenda_obj.item_servico.all().order_by('id')
                return render(request, 'lavajato_agenda/agenda_add_prazo.html', {'title':'Adicionar Prazo no Boleto', 'agenda_obj':agenda_obj, 'it_servicos':it_servicos})
            if request.method == 'POST' and request.POST.get('nova_data') != None:
                boleto = request.POST.get('nova_data')
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                agenda_obj.boleto = boleto
                agenda_obj.save()
                agenda_obj = agenda.objects.filter(id=agenda_obj.id).get()
                it_servicos = agenda_obj.item_servico.all().order_by('id')
                msg = "Data do boleto alterada com sucesso."
                return render(request, 'lavajato_agenda/agenda_add_prazo.html', {'title':'Adicionar Prazo no Boleto', 'agenda_obj':agenda_obj, 'msg':msg, 'it_servicos':it_servicos})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def agenda_ultima_ordem(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            if request.method == 'POST' and request.POST.get('cliente_id') != None:
                cliente_id = request.POST.get('cliente_id')
                try:
                    agenda_obj = agenda.objects.filter(cli__id=cliente_id).latest('id')
                    it_servicos = agenda_obj.item_servico.all()
                    hoje = datetime.now().strftime('%d/%m/%Y')
                    return render(request, 'lavajato_agenda/agenda_ultima_ordem.html', {'title':'Ultima Ordem do Cliente', 'agenda_obj':agenda_obj, 'it_servicos':it_servicos, 'hoje':hoje})
                except:
                    agenda_obj = None
                    hoje = datetime.now().strftime('%d/%m/%Y')
                    msg = "Cliente sem ordem aberta!"
                    return render(request, 'lavajato_agenda/agenda_ultima_ordem.html', {'title':'Ultima Ordem do Cliente', 'agenda_obj':agenda_obj, 'hoje':hoje, 'msg':msg})

            return render(request, 'lavajato_agenda/agenda_ultima_ordem.html', {'title':'Visualizar Ordem', 'agendas':agendas, 'servicos':servicos, 'funcionarios':funcionarios})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def ordem_branco(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            agenda_obj = None
            hoje = datetime.now().strftime('%d/%m/%Y')
            msg = "Cliente sem ordem aberta!"
            return render(request, 'lavajato_agenda/agenda_ultima_ordem.html', {'title':'Ordem do Cliente', 'agenda_obj':agenda_obj, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def pag_parcial(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            agenda_obj = None
            hoje = datetime.now().strftime('%d/%m/%Y')
            msg = "Cliente sem ordem aberta!"
            return render(request, 'lavajato_agenda/agenda_pagamento_parcial.html', {'title':'Pagamento Parcial', 'agenda_obj':agenda_obj, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})