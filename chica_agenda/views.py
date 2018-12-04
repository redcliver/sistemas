from django.shortcuts import render
from django.utils import timezone
import datetime
from datetime import date
from decimal import *
from .models import agenda, servico_item
from chica_cliente.models import cliente
from chica_controle.models import funcionario, servico
from chica_caixa.models import caixa_geral

# Create your views here.
def novo(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            clientes = cliente.objects.all().order_by('nome')
            servicos = servico.objects.all().order_by('nome')
            funcionarios = funcionario.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('cliente_id') != None:
                cliente_id = request.POST.get('cliente_id')
                cliente_obj = cliente.objects.filter(id=cliente_id).get()
                servico_id = request.POST.get('servico_id')
                servico_obj = servico.objects.filter(id=servico_id).get()
                funcionario_id = request.POST.get('funcionario_id')
                funcionario_obj = funcionario.objects.filter(id=funcionario_id).get()
                data = request.POST.get('data')
                novo_serv_item = servico_item(serv=servico_obj, func=funcionario_obj)
                novo_serv_item.save()
                novo_agendamento = agenda(cli=cliente_obj, data = data, pagamento=4, total=0)
                novo_agendamento.save()
                novo_agendamento.item_servico.add(novo_serv_item)
                novo_agendamento.total = servico_obj.valor
                novo_agendamento.save()
                msg = cliente_obj.nome+" agendado com sucesso!"
                return render(request, 'chica_agenda/agenda_novo.html', {'title':'Novo Agendamento', 'msg':msg})
            return render(request, 'chica_agenda/agenda_novo.html', {'title':'Novo Agendamento', 'clientes':clientes, 'servicos':servicos, 'funcionarios':funcionarios})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def busca(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            hoje = datetime.date.today().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(pagamento=4).order_by('data')
            if request.method == 'POST' and request.POST.get('agenda_id') != None:
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id)
                servicos = servico.objects.all().order_by('nome')
                funcionarios = funcionario.objects.all().order_by('nome')
                it_servicos = agenda_obj.item_servico.all()
                return render(request, 'chica_agenda/agenda_add_servico.html', {'title':'Adicionar Servico', 'agenda_obj':agenda_obj, 'servicos':servicos, 'funcionarios':funcionarios})
            return render(request, 'chica_agenda/agenda_busca.html', {'title':'Editar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def add_servico(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            agendas = agenda.objects.filter(pagamento=4).order_by('data')
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
                agenda_obj.total = agenda_obj.total + servico_obj.valor
                agenda_obj.save()
                msg = agenda_obj.cli.nome+" editado com sucesso!"
                return render(request, 'chica_agenda/agenda_add_servico.html', {'title':'Adicionar Servico ', 'msg':msg, 'agendas':agendas, 'servicos':servicos, 'funcionarios':funcionarios})
            return render(request, 'chica_agenda/agenda_add_servico.html', {'title':'Adicionar Servico', 'agendas':agendas, 'servicos':servicos, 'funcionarios':funcionarios})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def edita(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            hoje = datetime.date.today().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(data__icontains=hoje, pagamento=4)
            if request.method == 'POST' and request.POST.get('data') != None:
                hoje = request.POST.get('data')
                agendas = agenda.objects.filter(data__icontains=hoje, pagamento=4)
                return render(request, 'chica_agenda/agenda_edita.html', {'title':'Editar Agenda', 'agendas':agendas, 'hoje':hoje})
            return render(request, 'chica_agenda/agenda_edita.html', {'title':'Editar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def visualiza(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            hoje = datetime.date.today().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(data__icontains=hoje)
            if request.method == 'POST' and request.POST.get('data') != None:
                hoje = request.POST.get('data')
                agendas = agenda.objects.filter(data__icontains=hoje)
                return render(request, 'chica_agenda/agenda_visualiza.html', {'title':'Visualizar Agenda', 'agendas':agendas, 'hoje':hoje})
            return render(request, 'chica_agenda/agenda_visualiza.html', {'title':'Visualizar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def confirmacao(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            if request.method == 'POST' and request.POST.get('agenda_id') != None:
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                servicos = agenda_obj.item_servico.all()
                return render(request, 'chica_agenda/agenda_confirmacao.html', {'title':'Confirmar Agenda', 'agenda_obj':agenda_obj, 'servicos':servicos})
            return render(request, 'chica_agenda/agenda_visualiza.html', {'title':'Visualizar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def dinheiro(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            if request.method == 'GET' and request.GET.get('agenda_id') != None:
                agenda_id = request.GET.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                return render(request, 'chica_agenda/agenda_troco.html', {'title':'Troco', 'agenda_obj':agenda_obj})
            if request.method == 'POST' and request.POST.get('recebido') != None and request.POST.get('agenda_id') != None:
                agenda_id = request.POST.get('agenda_id')
                recebido = request.POST.get('recebido')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                troco = agenda_obj.total - Decimal(recebido)
                agenda_obj.pagamento = 1
                agenda_obj.save()
                caixa = caixa_geral.objects.latest('id')
                ultimo_id = caixa.id_operacao
                ultimo_id = int(ultimo_id) + 1
                novo_total = caixa.total + agenda_obj.total
                valor = agenda_obj.total
                desc = "Agendamento N:" + str(agenda_obj.id)
                nova_entrada = caixa_geral(operacao=1, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                nova_entrada.save()
                msg = "Pagamento do agendamento "+str(agenda_obj.id)+ "concluido com sucesso."
                return render(request, 'chica_agenda/agenda_troco.1.html', {'title':'Confirmar Agenda', 'agenda_obj':agenda_obj, 'troco':troco, 'recebido':recebido})
            return render(request, 'chica_agenda/agenda_visualiza.html', {'title':'Visualizar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})