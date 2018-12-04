from django.shortcuts import render
from .models import funcionario

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
                    name = request.POST.get('nome')
                    telefone = request.POST.get('tel')
                    celular = request.POST.get('cel')
                    email = request.POST.get('mail')
                    data_nasc = request.POST.get('data_nasc')
                    novo_funcionario = funcionario(nome=name, telefone=telefone, celular=celular, data_nasc = data_nasc, email=email)
                    novo_funcionario.save()
                    msg = name+" salvo com sucesso!"
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