from django.shortcuts import render
from django.utils import timezone
import datetime
from datetime import date
from .models import agenda
from chica_cliente.models import cliente
from chica_controle.models import funcionario, servico

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
                novo_agendamento = agenda(cli=cliente_obj, serv=servico_obj, func=funcionario_obj, data = data, pagamento=4)
                novo_agendamento.save()
                msg = cliente_obj.nome+" agendado com sucesso!"
                return render(request, 'chica_agenda/agenda_novo.html', {'title':'Novo Agendamento', 'msg':msg})
            return render(request, 'chica_agenda/agenda_novo.html', {'title':'Novo Agendamento', 'clientes':clientes, 'servicos':servicos, 'funcionarios':funcionarios})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})


def edita(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            hoje = datetime.date.today().strftime('%Y-%m-%d')
            agendas = agenda.objects.filter(data__icontains=hoje, estado=4)
            if request.method == 'POST' and request.POST.get('data') != None:
                hoje = request.POST.get('data')
                agendas = agenda.objects.filter(data__icontains=hoje, estado=4)
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
