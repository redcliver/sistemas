from django.shortcuts import render
from django.utils import timezone
import datetime
from datetime import date , timedelta
from decimal import *
from .models import agenda, servico_item, conta_parcelada, parcela
from lavajato_cliente.models import cliente
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
                return render(request, 'lavajato_agenda/agenda_novo.html', {'title':'Novo Agendamento', 'msg':msg})
            return render(request, 'lavajato_agenda/agenda_novo.html', {'title':'Novo Agendamento', 'clientes':clientes, 'servicos':servicos, 'funcionarios':funcionarios})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def busca(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = datetime.date.today().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(pagamento=4).order_by('data')
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
                it_servicos = agenda_obj.item_servico.all()
                msg = agenda_obj.cli.nome+" editado com sucesso!"
                return render(request, 'lavajato_agenda/agenda_add_servico.html', {'title':'Adicionar Servico ', 'it_servicos':it_servicos, 'msg':msg, 'agenda_obj':agenda_obj, 'servicos':servicos, 'funcionarios':funcionarios})
            return render(request, 'lavajato_agenda/agenda_add_servico.html', {'title':'Adicionar Servico', 'agendas':agendas, 'servicos':servicos, 'funcionarios':funcionarios})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def edita(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = datetime.date.today().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(data__icontains=hoje)
            if request.method == 'POST' and request.POST.get('data') != None:
                hoje = request.POST.get('data')
                agendas = agenda.objects.filter(data__icontains=hoje)
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
            hoje = datetime.date.today().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(data__icontains=hoje)
            if request.method == 'POST' and request.POST.get('servico_item_id') != None and request.POST.get('agenda_id') != None:
                servico_item_id = request.POST.get('servico_item_id')
                servico_item_obj = servico_item.objects.filter(id=servico_item_id).get()
                servico_item_obj.cancelado = 2
                servico_item_obj.serv.valor = servico_item_obj.serv.valor * -1
                servico_item_obj.save()
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
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
            hoje = datetime.date.today().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(data__icontains=hoje)
            if request.method == 'POST' and request.POST.get('data') != None:
                hoje = request.POST.get('data')
                agendas = agenda.objects.filter(data__icontains=hoje)
                return render(request, 'lavajato_agenda/agenda_visualiza.html', {'title':'Visualizar Agenda', 'agendas':agendas, 'hoje':hoje})
            return render(request, 'lavajato_agenda/agenda_visualiza.html', {'title':'Visualizar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def confirmacao(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            if request.method == 'POST' and request.POST.get('agenda_id') != None:
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                servicos = agenda_obj.item_servico.all()
                return render(request, 'lavajato_agenda/agenda_confirmacao.html', {'title':'Confirmar Agenda', 'agenda_obj':agenda_obj, 'servicos':servicos})
            return render(request, 'lavajato_agenda/agenda_visualiza.html', {'title':'Visualizar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def desmarcar(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = datetime.date.today().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(data__icontains=hoje)
            if request.method == 'POST' and request.POST.get('agenda_id') != None:
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                agenda_obj.pagamento = 5
                agenda_obj.save()
                msg = "Agendamento numero "+str(agenda_obj.id)+" desmarcado com sucesso."
                hoje = datetime.date.today().strftime('%Y-%m-%d')
                agendas = agenda.objects.filter(data__icontains=hoje)
                return render(request, 'lavajato_agenda/agenda_visualiza.html', {'title':'Desmarcar Agendamento', 'agendas':agendas, 'hoje':hoje, 'agenda_obj':agenda_obj, 'msg':msg})
            return render(request, 'lavajato_agenda/agenda_visualiza.html', {'title':'Visualizar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def dinheiro(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            if request.method == 'GET' and request.GET.get('agenda_id') != None:
                agenda_id = request.GET.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                return render(request, 'lavajato_agenda/agenda_troco.html', {'title':'Troco', 'agenda_obj':agenda_obj})
            if request.method == 'POST' and request.POST.get('recebido') != None and request.POST.get('agenda_id') != None:
                agenda_id = request.POST.get('agenda_id')
                recebido = request.POST.get('recebido')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                troco = agenda_obj.total - Decimal(recebido)
                troco= troco * -1
                agenda_obj.pagamento = 1
                agenda_obj.save()
                caixa = caixa_geral.objects.latest('id')
                ultimo_id = agenda_obj.id
                novo_total = caixa.total + agenda_obj.total
                valor = agenda_obj.total
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
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                agenda_obj.pagamento = 2
                agenda_obj.save()
                caixa = caixa_geral.objects.latest('id')
                ultimo_id = agenda_obj.id
                novo_total = caixa.total + agenda_obj.total
                valor = agenda_obj.total
                desc = "Agendamento N:" + str(agenda_obj.id)
                nova_entrada = caixa_geral(operacao=1, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                nova_entrada.save()
                msg = "Pagamento do agendamento "+str(agenda_obj.id)+ " concluido com sucesso."
                total_msg = "Total: R$"+ str(valor)
                return render(request, 'lavajato_homr/home.html', {'title':'Home', 'msg':msg, 'total_msg':total_msg})
            return render(request, 'lavajato_agenda/agenda_visualiza.html', {'title':'Visualizar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def credito(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = datetime.date.today().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(data__icontains=hoje)
            if request.method == 'POST' and request.POST.get('agenda_id') != None and request.POST.get('n_parcelas') == '1':
                d = timedelta(days=30)
                hoje = datetime.date.today()
                data_pag = hoje + d
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                agenda_obj.pagamento = 3
                agenda_obj.save()
                nova_parcela = parcela(estado=1, valor=agenda_obj.total, data=data_pag)
                nova_parcela.save()
                nova_conta_parcelada = conta_parcelada(referente=agenda_obj, parcelas_total=1)
                nova_conta_parcelada.save()
                nova_conta_parcelada.parcelas.add(nova_parcela)
                nova_conta_parcelada.save()
                msg = "Pagamento do agendamento "+str(agenda_obj.id)+ " concluido com sucesso."
                return render(request, 'lavajato_home/home.html', {'title':'Home', 'msg':msg})
            if request.method == 'POST' and request.POST.get('agenda_id') != None and request.POST.get('n_parcelas') != '1':
                d = timedelta(days=30)
                p = 0
                hoje = datetime.date.today()
                data_pag = hoje + d
                n_parcelas = request.POST.get('n_parcelas')
                agenda_id = request.POST.get('agenda_id')
                agenda_obj = agenda.objects.filter(id=agenda_id).get()
                nova_conta_parcelada = conta_parcelada(referente=agenda_obj, parcelas_total=n_parcelas)
                nova_conta_parcelada.save()
                parc_valor = agenda_obj.total / int(n_parcelas)
                while p < int(n_parcelas):
                    d = timedelta(days=30)
                    d = d * p
                    hoje = datetime.date.today()
                    data_pag = hoje + d
                    nova_parcela = parcela(estado=1, valor=parc_valor, data=data_pag)
                    nova_parcela.save()
                    nova_conta_parcelada.parcelas.add(nova_parcela)
                    nova_conta_parcelada.save()
                    p = p + 1
                agenda_obj.pagamento = 3
                agenda_obj.save()
                msg = "Pagamento do agendamento "+str(agenda_obj.id)+ " concluido com sucesso."
                return render(request, 'lavajato_home/home.html', {'title':'Home', 'msg':msg})
            return render(request, 'lavajato_agenda/agenda_visualiza.html', {'title':'Visualizar Agenda', 'agendas':agendas, 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})