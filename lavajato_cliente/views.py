from django.shortcuts import render
import datetime
from .models import cliente, carro
# Create your views here.
def lavajato_cliente(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            if request.method == 'POST' and request.POST.get('nome') != None:
                name = request.POST.get('nome')
                telefone = request.POST.get('tel')
                celular = request.POST.get('cel')
                email = request.POST.get('mail')
                data_nasc = request.POST.get('data_nasc')
                novo_cliente = cliente(nome=name, telefone=telefone, celular=celular, data_nasc = data_nasc, email=email)
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
                mail = request.POST.get('mail')
                data_nasc = request.POST.get('data_nasc')
                cliente_obj.nome = nome
                cliente_obj.telefone = tel
                cliente_obj.celular = cel
                cliente_obj.email = mail
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
                return render(request, 'lavajato_cliente/cliente_novo_carro.html', {'title':'Novo Carro', 'cliente_obj':cliente_obj, 'cars':cars})
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
                return render(request, 'lavajato_cliente/cliente_novo_carro.html', {'title':'Novo Carro', 'cliente_obj':cliente_obj, 'cars':cars, 'msg':msg})
            return render(request, 'lavajato_cliente/cliente_busca_novo_carro.html', {'title':'Novo Carro'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})