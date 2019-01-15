from django.shortcuts import render
import datetime
from .models import cliente, carro
from lavajato_agenda.models import agenda
# Create your views here.
def lavajato_cliente(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            if request.method == 'POST' and request.POST.get('nome') != None:
                name = request.POST.get('nome')
                telefone = request.POST.get('tel')
                celular = request.POST.get('cel')
                cpf = request.POST.get('cpf')
                email = request.POST.get('mail')
                endereco = request.POST.get('endereco')
                numero = request.POST.get('numero')
                bairro = request.POST.get('bairro')
                cidade = request.POST.get('cidade')
                uf_cidade = request.POST.get('uf_cidade')
                data_nasc = request.POST.get('data_nasc')
                novo_cliente = cliente(nome=name, telefone=telefone, celular=celular, data_nasc = data_nasc, cpf=cpf, email=email, endereco=endereco, numero=numero, bairro=bairro, cidade=cidade, uf_cidade=uf_cidade)
                novo_cliente.save()
                if request.POST.get('modelo') != None:
                    modelo = request.POST.get('modelo')
                    placa = request.POST.get('placa')
                    cor = request.POST.get('cor')
                    observacao = request.POST.get('observacao')
                    novo_carro = carro(modelo=modelo, placa=placa, cor=cor, observacao=observacao)
                    novo_carro.save()
                    novo_cliente.carros.add(novo_carro)
                    novo_cliente.save()
                    msg = name+" salvo com sucesso!"
                    return render(request, 'lavajato_cliente/cliente_novo.html', {'title':'Novo Cliente', 'msg':msg})
                return render(request, 'lavajato_cliente/cliente_novo.html', {'title':'Novo Cliente', 'msg':msg})
            return render(request, 'lavajato_cliente/cliente_novo.html', {'title':'Novo Cliente'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def busca(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            clientes = cliente.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('cliente_id') != None:
                cliente_id = request.POST.get('cliente_id')
                cliente_obj = cliente.objects.get(id=cliente_id)
                return render(request, 'lavajato_cliente/cliente_visualizar.html', {'title':'Visualizar Cliente', 'cliente_obj':cliente_obj})
            return render(request, 'lavajato_cliente/cliente_busca.html', {'title':'Buscar Cliente', 'clientes':clientes})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def edita(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            clientes = cliente.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('cliente_id') != None:
                cliente_id = request.POST.get('cliente_id')
                cliente_obj = cliente.objects.get(id=cliente_id)
                return render(request, 'lavajato_cliente/cliente_edita.html', {'title':'Visualizar Cliente', 'cliente_obj':cliente_obj})
            return render(request, 'lavajato_cliente/cliente_busca_edita.html', {'title':'Editar Cliente', 'clientes':clientes})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def salva(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            clientes = cliente.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('cliente_id') != None:
                cliente_id = request.POST.get('cliente_id')
                cliente_obj = cliente.objects.get(id=cliente_id)
                nome = request.POST.get('nome')
                tel = request.POST.get('tel')
                cel = request.POST.get('cel')
                cpf = request.POST.get('cpf')
                mail = request.POST.get('mail')
                endereco = request.POST.get('endereco')
                numero = request.POST.get('numero')
                bairro = request.POST.get('bairro')
                cidade = request.POST.get('cidade')
                uf_cidade = request.POST.get('uf_cidade')
                data_nasc = request.POST.get('data_nasc')
                cliente_obj.nome = nome
                cliente_obj.telefone = tel
                cliente_obj.celular = cel
                cliente_obj.cpf = cpf
                cliente_obj.email = mail
                cliente_obj.endereco = endereco
                cliente_obj.numero = numero
                cliente_obj.bairro = bairro
                cliente_obj.cidade = cidade
                cliente_obj.uf_cidade = uf_cidade
                cliente_obj.data_nasc = data_nasc
                cliente_obj.save()
                msg = cliente_obj.nome + " editado(a) com sucesso!"
                return render(request, 'lavajato_cliente/cliente_busca_edita.html', {'title':'Editar Cliente', 'clientes':clientes, 'msg':msg})
            return render(request, 'lavajato_cliente/cliente_busca_edita.html', {'title':'Editar Cliente', 'clientes':clientes})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def novo_carro(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            clientes = cliente.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('cliente_id') != None and request.POST.get('modelo') == None:
                cliente_id = request.POST.get('cliente_id')
                cliente_obj = cliente.objects.get(id=cliente_id)
                cars = cliente_obj.carros.all().order_by('modelo')
                return render(request, 'lavajato_cliente/cliente_novo_carro.html', {'title':'Novo Veiculo', 'cliente_obj':cliente_obj, 'cars':cars})
            if request.method == 'POST' and request.POST.get('cliente_id') != None and request.POST.get('modelo') != None:
                cliente_id = request.POST.get('cliente_id')
                cliente_obj = cliente.objects.get(id=cliente_id)
                modelo = request.POST.get('modelo')
                placa = request.POST.get('placa')
                cor = request.POST.get('cor')
                observacao = request.POST.get('observacao')
                novo_carro = carro(modelo=modelo, placa=placa, cor=cor, observacao=observacao)
                novo_carro.save()
                cliente_obj.carros.add(novo_carro)
                cliente_obj.save()
                cars = cliente_obj.carros.all().order_by('modelo')
                msg = modelo+" salvo com sucesso!"
                return render(request, 'lavajato_cliente/cliente_novo_carro.html', {'title':'Novo Veiculo', 'cliente_obj':cliente_obj, 'cars':cars, 'msg':msg})
            return render(request, 'lavajato_cliente/cliente_busca_novo_carro.html', {'title':'Novo Veiculo', 'clientes':clientes})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def carro_edita(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            clientes = cliente.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('carro_id') != None:
                cliente_id = request.POST.get('cliente_id')
                cliente_obj = cliente.objects.get(id=cliente_id)
                carro_id = request.POST.get('carro_id')
                carro_obj = carro.objects.get(id=carro_id)
                return render(request, 'lavajato_cliente/edita_carro.html', {'title':'Editar Veiculo', 'cliente_obj':cliente_obj, 'carro_obj':carro_obj})
            if request.method == 'POST' and request.POST.get('cliente_id') != None:
                cliente_id = request.POST.get('cliente_id')
                cliente_obj = cliente.objects.get(id=cliente_id)
                cars = cliente_obj.carros.all().order_by('modelo')
                return render(request, 'lavajato_cliente/seleciona_carro.html', {'title':'Selecione o Veiculo', 'cliente_obj':cliente_obj, 'cars':cars})
            return render(request, 'lavajato_cliente/busca_edita_carro.html', {'title':'Editar Veiculo', 'clientes':clientes})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def carro_salva_edita(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            clientes = cliente.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('cliente_id') != None and request.POST.get('carro_id') != None:
                cliente_id = request.POST.get('cliente_id')
                cliente_obj = cliente.objects.get(id=cliente_id)
                carro_id = request.POST.get('carro_id')
                carro_obj = carro.objects.get(id=carro_id)
                modelo = request.POST.get('modelo')
                placa = request.POST.get('placa')
                cor = request.POST.get('cor')
                observacao = request.POST.get('observacao')
                carro_obj.modelo = modelo
                carro_obj.placa = placa
                carro_obj.cor = cor
                carro_obj.observacao = observacao
                carro_obj.save()
                msg = modelo+" alterado com sucesso!"
                cars = cliente_obj.carros.all().order_by('modelo')
                return render(request, 'lavajato_cliente/seleciona_carro.html', {'title':'Selecione o Veiculo', 'cliente_obj':cliente_obj, 'cars':cars})
            return render(request, 'lavajato_cliente/busca_edita_carro.html', {'title':'Editar Veiculo', 'clientes':clientes})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def fechamento_mensal(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            clientes = cliente.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('cliente_id') != None and request.POST.get('mes') != None:
                aberto = 0 
                pago = 0
                desmarcado = 0
                cliente_id = request.POST.get('cliente_id')
                mes = request.POST.get('mes')
                cliente_obj = cliente.objects.get(id=cliente_id)
                agendas = agenda.objects.filter(cli=cliente_obj, data__month=mes).all()
                for a in agenda.objects.filter(cli=cliente_obj, data__month=mes, estado=1).all():
                    aberto = aberto + a.total
                for b in agenda.objects.filter(cli=cliente_obj, data__month=mes, estado=2).all():
                    desmarcado = desmarcado + b.total
                for c in agenda.objects.filter(cli=cliente_obj, data__month=mes, estado=3).all():
                    pago = pago + c.total
                
                return render(request, 'lavajato_cliente/cliente_confirma_fechamento.html', {'title':'Fechamento Cliente', 'cliente_obj':cliente_obj, 'agendas':agendas, 'aberto':aberto, 'pago':pago, 'desmarcado':desmarcado, 'mes':mes})
            return render(request, 'lavajato_cliente/cliente_fechamento.html', {'title':'Fechamento Cliente', 'clientes':clientes})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def pagamento_geral(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            clientes = cliente.objects.all().order_by('nome')
            if request.method == 'GET' and request.GET.get('cliente_id') != None and request.GET.get('mes_cli') != None:
                aberto = 0
                cliente_id = request.GET.get('cliente_id')
                mes_cli = request.GET.get('mes_cli')
                cliente_obj = cliente.objects.get(id=cliente_id)
                agendas = agenda.objects.filter(cli=cliente_obj, data__month=mes_cli, estado=1).all()
                for a in agenda.objects.filter(cli=cliente_obj, data__month=mes_cli, estado=1).all():
                    aberto = aberto + a.total
                return render(request, 'lavajato_cliente/cliente_fechar_os.html', {'title':'Fechamento Cliente', 'cliente_obj':cliente_obj, 'agendas':agendas, 'aberto':aberto, 'mes_cli':mes_cli})
            if request.method == 'POST' and request.POST.get('cliente_id') != None and request.POST.get('mes_cli') != None:
                aberto = 0 
                pago = 0
                desmarcado = 0
                cliente_id = request.POST.get('cliente_id')
                mes_cli = request.POST.get('mes_cli')
                cliente_obj = cliente.objects.get(id=cliente_id)
                agendas = agenda.objects.filter(cli=cliente_obj, data__month=mes_cli).all()
                for a in agenda.objects.filter(cli=cliente_obj, data__month=mes_cli, estado=1).all():
                    aberto = aberto + a.total
                for b in agenda.objects.filter(cli=cliente_obj, data__month=mes_cli, estado=2).all():
                    desmarcado = desmarcado + b.total
                for c in agenda.objects.filter(cli=cliente_obj, data__month=mes_cli, estado=3).all():
                    pago = pago + c.total
                return render(request, 'lavajato_cliente/cliente_confirma_fechamento.html', {'title':'Fechamento Cliente', 'cliente_obj':cliente_obj, 'agendas':agendas, 'aberto':aberto, 'pago':pago, 'desmarcado':desmarcado})
            return render(request, 'lavajato_cliente/cliente_fechamento.html', {'title':'Fechamento Cliente', 'clientes':clientes})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})