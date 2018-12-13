from django.shortcuts import render
from .models import funcionario, servico, reg_ponto
from django.utils import timezone
from datetime import datetime

# Create your views here.
def chica_controle(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'chicadiniz':
            if cargo == 'boss':
                return render(request, 'chica_controle/controle.html', {'title':'Controle'})
            return render(request, 'chica_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
def novo_funcionario(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'chicadiniz':
            if cargo == 'boss':
                if request.method == 'POST' and request.POST.get('nome') != None:
                    nome = request.POST.get('nome')
                    telefone = request.POST.get('tel')
                    celular = request.POST.get('cel')
                    email = request.POST.get('mail')
                    data_nasc = request.POST.get('data_nasc')
                    novo_funcionario = funcionario(nome=nome, telefone=telefone, celular=celular, data_nasc = data_nasc, email=email)
                    novo_funcionario.save()
                    msg = nome+" salvo com sucesso!"
                    return render(request, 'chica_controle/funcionario_novo.html', {'title':'Novo funcionario', 'msg':msg})
                return render(request, 'chica_controle/funcionario_novo.html', {'title':'Novo funcionario'})
            return render(request, 'chica_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def busca_funcionario(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'chicadiniz':
            if cargo == 'boss':
                funcionarios = funcionario.objects.all().order_by('nome')
                if request.method == 'POST' and request.POST.get('funcionario_id') != None:
                    funcionario_id = request.POST.get('funcionario_id')
                    funcionario_obj = funcionario.objects.get(id=funcionario_id)
                    return render(request, 'chica_controle/funcionario_visualizar.html', {'title':'Visualizar Funcionario', 'funcionario_obj':funcionario_obj})
                return render(request, 'chica_controle/funcionario_busca.html', {'title':'Buscar Funcionario', 'funcionarios':funcionarios})
            return render(request, 'chica_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def edita_funcionario(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'chicadiniz':
            if cargo == 'boss':
                funcionarios = funcionario.objects.all().order_by('nome')
                if request.method == 'POST' and request.POST.get('funcionario_id') != None:
                    funcionario_id = request.POST.get('funcionario_id')
                    funcionario_obj = funcionario.objects.get(id=funcionario_id)
                    return render(request, 'chica_controle/funcionario_edita.html', {'title':'Visualizar Funcionario', 'funcionario_obj':funcionario_obj})
                return render(request, 'chica_controle/funcionario_busca_edita.html', {'title':'Editar Funcionario', 'funcionarios':funcionarios})
            return render(request, 'chica_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def salva_funcionario(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'chicadiniz':
            if cargo == 'boss':
                funcionarios = funcionario.objects.all().order_by('nome')
                if request.method == 'POST' and request.POST.get('funcionario_id') != None:
                    funcionario_id = request.POST.get('funcionario_id')
                    funcionario_obj = funcionario.objects.get(id=funcionario_id)
                    nome = request.POST.get('nome')
                    tel = request.POST.get('tel')
                    cel = request.POST.get('cel')
                    mail = request.POST.get('mail')
                    data_nasc = request.POST.get('data_nasc')
                    funcionario_obj.nome = nome
                    funcionario_obj.telefone = tel
                    funcionario_obj.celular = cel
                    funcionario_obj.email = mail
                    funcionario_obj.data_nasc = data_nasc
                    funcionario_obj.save()
                    msg = funcionario_obj.nome + " editado(a) com sucesso!"
                    return render(request, 'chica_controle/funcionario_busca_edita.html', {'title':'Editar Funcionario', 'funcionarios':funcionarios, 'msg':msg})
                return render(request, 'chica_controle/funcionario_busca_edita.html', {'title':'Editar Funcionario', 'funcionarios':funcionarios})
            return render(request, 'chica_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def novo_servico(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'chicadiniz':
            if cargo == 'boss':
                if request.method == 'POST' and request.POST.get('nome') != None:
                    nome = request.POST.get('nome')
                    valor = request.POST.get('valor')
                    descricao = request.POST.get('descricao')
                    novo_servico = servico(nome=nome, valor=valor, descricao=descricao)
                    novo_servico.save()
                    msg = nome+" salvo com sucesso!"
                    return render(request, 'chica_controle/servico_novo.html', {'title':'Novo Servico', 'msg':msg})
                return render(request, 'chica_controle/servico_novo.html', {'title':'Novo Servico'})
            return render(request, 'chica_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def busca_servico(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'chicadiniz':
            if cargo == 'boss':
                servicos = servico.objects.all().order_by('nome')
                if request.method == 'POST' and request.POST.get('servico_id') != None:
                    servico_id = request.POST.get('servico_id')
                    servico_obj = servico.objects.get(id=servico_id)
                    return render(request, 'chica_controle/servico_visualizar.html', {'title':'Visualizar Servico', 'servico_obj':servico_obj})
                return render(request, 'chica_controle/servico_busca.html', {'title':'Buscar Servico', 'servicos':servicos})
            return render(request, 'chica_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def edita_servico(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'chicadiniz':
            if cargo == 'boss':
                servicos = servico.objects.all().order_by('nome')
                if request.method == 'POST' and request.POST.get('servico_id') != None:
                    servico_id = request.POST.get('servico_id')
                    servico_obj = servico.objects.get(id=servico_id)
                    return render(request, 'chica_controle/servico_edita.html', {'title':'Visualizar Servico', 'servico_obj':servico_obj})
                return render(request, 'chica_controle/servico_busca_edita.html', {'title':'Editar Servico', 'servicos':servicos})
            return render(request, 'chica_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def salva_servico(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'chicadiniz':
            if cargo == 'boss':
                servicos = servico.objects.all().order_by('nome')
                if request.method == 'POST' and request.POST.get('servico_id') != None:
                    servico_id = request.POST.get('servico_id')
                    servico_obj = servico.objects.get(id=servico_id)
                    nome = request.POST.get('nome')
                    valor = request.POST.get('valor')
                    descricao = request.POST.get('descricao')
                    servico_obj.nome = nome
                    servico_obj.valor = valor
                    servico_obj.descricao = descricao
                    servico_obj.save()
                    msg = servico_obj.nome + " editado(a) com sucesso!"
                    return render(request, 'chica_controle/servico_busca_edita.html', {'title':'Editar Servico', 'servicos':servicos, 'msg':msg})
                return render(request, 'chica_controle/servico_busca_edita.html', {'title':'Editar Servico', 'servicos':servicos})
            return render(request, 'chica_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def ponto(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'chicadiniz':
            if cargo == 'funcionario':
                if request.method == 'POST' and request.POST.get('entrada') != None:
                    func = request.user.get_short_name()##alterar para username
                    novo_registro = reg_ponto(estado = 1, operacao = 1, funcionario = func)
                    novo_registro.save()
                    msg = "Ponto registrado com sucesso!"
                    return render(request, 'chica_controle/registro_ponto.html', {'title':'Registro de Ponto', 'msg':msg})
                if request.method == 'POST' and request.POST.get('saida') != None:
                    func = request.user.get_short_name()##alterar para username
                    novo_registro = reg_ponto(estado = 1, operacao = 2, funcionario = func)
                    novo_registro.save()
                    msg = "Ponto registrado com sucesso!"
                    return render(request, 'chica_controle/registro_ponto.html', {'title':'Registro de Ponto', 'msg':msg})
                return render(request, 'chica_controle/registro_ponto.html', {'title':'Registro de Ponto'})
            if cargo == 'boss':
                try:
                    pendencias = reg_ponto.objects.filter(estado=1).count()
                except:
                    pendencias = 0
                return render(request, 'chica_controle/ponto_boss.html', {'title':'Ponto', 'pendencias':pendencias})
            return render(request, 'chica_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def confirma_ponto(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'chicadiniz':
            if cargo == 'boss':
                ponto_aberto = reg_ponto.objects.filter(estado = 1).order_by("data_cadastro")
                if request.method == 'POST' and request.POST.get('reg_ponto_id') != None:
                    reg_ponto_id = request.POST.get('reg_ponto_id')
                    hoje = timezone.now()
                    ponto_obj = reg_ponto.objects.get(id=reg_ponto_id)
                    ponto_obj.estado = 2
                    ponto_obj.data_confirmacao = hoje
                    ponto_obj.save()
                    msg = "Ponto confirmado com sucesso!"
                    return render(request, 'chica_controle/confirmacao_ponto.html', {'title':'Confirmacao de Ponto', 'ponto_aberto':ponto_aberto, 'msg':msg})
                return render(request, 'chica_controle/confirmacao_ponto.html', {'title':'Confirmacao de Ponto', 'ponto_aberto':ponto_aberto})
            return render(request, 'chica_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})