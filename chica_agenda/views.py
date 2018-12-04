from django.shortcuts import render
import datetime
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
                hora = request.POST.get('hora')
                horario = datetime.combine(data, hora)
                novo_agendamento = agenda(cli=cliente_obj, serv=servico_obj, func=funcionario_obj, data = horario)
                novo_agendamento.save()
                msg = name+" agendado com sucesso!"
                return render(request, 'chica_agenda/agenda_novo.html', {'title':'Novo Agendamento', 'msg':msg})
            return render(request, 'chica_agenda/agenda_novo.html', {'title':'Novo Agendamento', 'clientes':clientes, 'servicos':servicos, 'funcionarios':funcionarios})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def busca(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            clientes = cliente.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('cliente_id') != None:
                cliente_id = request.POST.get('cliente_id')
                cliente_obj = cliente.objects.get(id=cliente_id)
                return render(request, 'chica_cliente/cliente_visualizar.html', {'title':'Visualizar Cliente', 'cliente_obj':cliente_obj})
            return render(request, 'chica_cliente/cliente_busca.html', {'title':'Buscar Cliente', 'clientes':clientes})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def edita(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            clientes = cliente.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('cliente_id') != None:
                cliente_id = request.POST.get('cliente_id')
                cliente_obj = cliente.objects.get(id=cliente_id)
                return render(request, 'chica_cliente/cliente_edita.html', {'title':'Visualizar Cliente', 'cliente_obj':cliente_obj})
            return render(request, 'chica_cliente/cliente_busca_edita.html', {'title':'Editar Cliente', 'clientes':clientes})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def visualiza(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            clientes = cliente.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('cliente_id') != None:
                cliente_id = request.POST.get('cliente_id')
                cliente_obj = cliente.objects.get(id=cliente_id)
                nome = request.POST.get('nome')
                tel = request.POST.get('tel')
                cel = request.POST.get('cel')
                mail = request.POST.get('mail')
                data_nasc = request.POST.get('data_nasc')
                cliente_obj.nome = nome
                cliente_obj.telefone = tel
                cliente_obj.celular = cel
                cliente_obj.email = mail
                cliente_obj.data_nasc = data_nasc
                cliente_obj.save()
                msg = cliente_obj.nome + " editado(a) com sucesso!"
                return render(request, 'chica_cliente/cliente_busca_edita.html', {'title':'Editar Cliente', 'clientes':clientes, 'msg':msg})
            return render(request, 'chica_cliente/cliente_busca_edita.html', {'title':'Editar Cliente', 'clientes':clientes})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
