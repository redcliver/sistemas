from django.shortcuts import render
from .models import conta

# Create your views here.
def chica_conta(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            if request.method == 'POST' and request.POST.get('nome') != None:
                nome = request.POST.get('nome')
                valor = request.POST.get('valor')
                data_venc = request.POST.get('data_venc')
                nova_conta = conta(nome=nome, valor=valor, data_venc=data_venc, estado=1)
                nova_conta.save()
                msg = nome +" cadastrado(a) com sucesso!"
                return render(request, 'chica_conta/conta_novo.html', {'title':'Nova Conta', 'msg':msg})
            return render(request, 'chica_conta/conta_novo.html', {'title':'Nova Conta'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def busca(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            contas = conta.objects.all().order_by('data_venc')
            if request.method == 'POST' and request.POST.get('conta_id') != None:
                conta_id = request.POST.get('conta_id')
                conta_obj = conta.objects.get(id=conta_id)
                return render(request, 'chica_conta/conta_visualizar.html', {'title':'Visualizar Conta', 'conta_obj':conta_obj})
            return render(request, 'chica_conta/conta_busca.html', {'title':'Buscar Conta', 'contas':contas})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def edita(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            contas = conta.objects.filter(estado=1).all().order_by('nome')
            if request.method == 'POST' and request.POST.get('conta_id') != None:
                conta_id = request.POST.get('conta_id')
                conta_obj = conta.objects.get(id=conta_id)
                return render(request, 'chica_conta/conta_edita.html', {'title':'Visualizar Conta', 'conta_obj':conta_obj})
            return render(request, 'chica_conta/conta_busca_edita.html', {'title':'Editar Conta', 'contas':contas})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def salva(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
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
                return render(request, 'chica_conta/conta_busca_edita.html', {'title':'Editar Conta', 'msg':msg, 'contas':contas})
            return render(request, 'chica_conta/conta_busca_edita.html', {'title':'Editar Conta'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def pagar(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            contas = conta.objects.filter(estado=1).all().order_by('data_venc')
            if request.method == 'POST' and request.POST.get('conta_id') != None:
                conta_id = request.POST.get('conta_id')
                conta_obj = conta.objects.get(id=conta_id)
                conta_obj.estado = 2
                conta_obj.save()
                msg = conta_obj.nome + " pago(a) com sucesso!"
                return render(request, 'chica_conta/conta_pagar.html', {'title':'Pagar Conta', 'contas':contas, 'msg':msg})
            return render(request, 'chica_conta/conta_pagar.html', {'title':'Pagar Conta', 'contas':contas})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})