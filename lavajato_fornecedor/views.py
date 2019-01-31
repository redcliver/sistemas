# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import fornecedor

# Create your views here.
def lavajato_fornecedor(request):
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
                novo_fornecedor = fornecedor(nome=name, telefone=telefone, celular=celular, cpf=cpf, email=email, endereco=endereco, numero=numero, bairro=bairro, cidade=cidade, uf_cidade=uf_cidade)
                novo_fornecedor.save()
                msg = name+" salvo com sucesso!"
                return render(request, 'lavajato_fornecedor/fornecedor_novo.html', {'title':'Novo Fornecedor','msg':msg})
            return render(request, 'lavajato_fornecedor/fornecedor_novo.html', {'title':'Novo Fornecedor'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def busca(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            fornecedores = fornecedor.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('fornecedor_id') != None:
                fornecedor_id = request.POST.get('fornecedor_id')
                fornecedor_obj = fornecedor.objects.get(id=fornecedor_id)
                return render(request, 'lavajato_fornecedor/fornecedor_visualiza.html', {'title':'Visualizar Fornecedor', 'fornecedor_obj':fornecedor_obj})
            return render(request, 'lavajato_fornecedor/fornecedor_busca.html', {'title':'Buscar Fornecedor', 'fornecedores':fornecedores})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def edita(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            fornecedores = fornecedor.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('fornecedor_id') != None:
                fornecedor_id = request.POST.get('fornecedor_id')
                fornecedor_obj = fornecedor.objects.get(id=fornecedor_id)
                return render(request, 'lavajato_fornecedor/fornecedor_edita.html', {'title':'Editar Fornecedor', 'fornecedor_obj':fornecedor_obj})
            return render(request, 'lavajato_fornecedor/fornecedor_busca_edita.html', {'title':'Editar Fornecedor', 'fornecedores':fornecedores})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def salva(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            fornecedores = fornecedor.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('fornecedor_id') != None:
                fornecedor_id = request.POST.get('fornecedor_id')
                fornecedor_obj = fornecedor.objects.get(id=fornecedor_id)
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
                bloqueado = request.POST.get('bloqueado')
                fornecedor_obj.nome = nome
                fornecedor_obj.telefone = tel
                fornecedor_obj.celular = cel
                fornecedor_obj.cpf = cpf
                fornecedor_obj.email = mail
                fornecedor_obj.endereco = endereco
                fornecedor_obj.numero = numero
                fornecedor_obj.bairro = bairro
                fornecedor_obj.cidade = cidade
                fornecedor_obj.uf_cidade = uf_cidade
                fornecedor_obj.estado = bloqueado
                fornecedor_obj.save()
                msg = fornecedor_obj.nome + " editado(a) com sucesso!"
                return render(request, 'lavajato_fornecedor/fornecedor_edita.html', {'title':'Editar Fornecedor', 'fornecedor_obj':fornecedor_obj, 'msg':msg})
            return render(request, 'lavajato_fornecedor/fornecedor_busca_edita.html', {'title':'Editar Fornecedor', 'fornecedores':fornecedores})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})