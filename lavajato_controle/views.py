from django.shortcuts import render
from .models import funcionario, servico, reg_ponto, conta_empresa
from django.utils import timezone
from decimal import *
from datetime import datetime
from datetime import timedelta
from lavajato_agenda.models import agenda
from django.contrib.auth.models import User

# Create your views here.
def chica_controle(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'dayson':
            if cargo == 'boss':
                return render(request, 'lavajato_controle/controle.html', {'title':'Controle'})
            if cargo == 'funcionario':
                return render(request, 'lavajato_controle/controle_funcionario.html', {'title':'Controle'})
            return render(request, 'lavajato_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def novo_funcionario(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'dayson':
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
                    return render(request, 'lavajato_controle/funcionario_novo.html', {'title':'Novo funcionario', 'msg':msg})
                return render(request, 'lavajato_controle/funcionario_novo.html', {'title':'Novo funcionario'})
            return render(request, 'chicalavajato_home_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def busca_funcionario(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'dayson':
            if cargo == 'boss':
                funcionarios = funcionario.objects.all().order_by('nome')
                if request.method == 'POST' and request.POST.get('funcionario_id') != None:
                    funcionario_id = request.POST.get('funcionario_id')
                    funcionario_obj = funcionario.objects.get(id=funcionario_id)
                    return render(request, 'lavajato_controle/funcionario_visualizar.html', {'title':'Visualizar Funcionario', 'funcionario_obj':funcionario_obj})
                return render(request, 'lavajato_controle/funcionario_busca.html', {'title':'Buscar Funcionario', 'funcionarios':funcionarios})
            return render(request, 'lavajato_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def edita_funcionario(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'dayson':
            if cargo == 'boss':
                funcionarios = funcionario.objects.all().order_by('nome')
                if request.method == 'POST' and request.POST.get('funcionario_id') != None:
                    funcionario_id = request.POST.get('funcionario_id')
                    funcionario_obj = funcionario.objects.get(id=funcionario_id)
                    return render(request, 'lavajato_controle/funcionario_edita.html', {'title':'Visualizar Funcionario', 'funcionario_obj':funcionario_obj})
                return render(request, 'lavajato_controle/funcionario_busca_edita.html', {'title':'Editar Funcionario', 'funcionarios':funcionarios})
            return render(request, 'lavajato_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def salva_funcionario(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'dayson':
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
                    return render(request, 'lavajato_controle/funcionario_busca_edita.html', {'title':'Editar Funcionario', 'funcionarios':funcionarios, 'msg':msg})
                return render(request, 'lavajato_controle/funcionario_busca_edita.html', {'title':'Editar Funcionario', 'funcionarios':funcionarios})
            return render(request, 'lavajato_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def novo_servico(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'dayson':
            if cargo == 'boss':
                if request.method == 'POST' and request.POST.get('nome') != None:
                    nome = request.POST.get('nome')
                    valor = request.POST.get('valor')
                    descricao = request.POST.get('descricao')
                    novo_servico = servico(nome=nome, valor=valor, descricao=descricao)
                    novo_servico.save()
                    msg = nome+" salvo com sucesso!"
                    return render(request, 'lavajato_controle/servico_novo.html', {'title':'Novo Servico', 'msg':msg})
                return render(request, 'lavajato_controle/servico_novo.html', {'title':'Novo Servico'})
            return render(request, 'lavajato_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def busca_servico(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'dayson':
            if cargo == 'boss':
                servicos = servico.objects.all().order_by('nome')
                if request.method == 'POST' and request.POST.get('servico_id') != None:
                    servico_id = request.POST.get('servico_id')
                    servico_obj = servico.objects.get(id=servico_id)
                    return render(request, 'lavajato_controle/servico_visualizar.html', {'title':'Visualizar Servico', 'servico_obj':servico_obj})
                return render(request, 'lavajato_controle/servico_busca.html', {'title':'Buscar Servico', 'servicos':servicos})
            return render(request, 'lavajato_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def edita_servico(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'dayson':
            if cargo == 'boss':
                servicos = servico.objects.all().order_by('nome')
                if request.method == 'POST' and request.POST.get('servico_id') != None:
                    servico_id = request.POST.get('servico_id')
                    servico_obj = servico.objects.get(id=servico_id)
                    return render(request, 'lavajato_controle/servico_edita.html', {'title':'Visualizar Servico', 'servico_obj':servico_obj})
                return render(request, 'lavajato_controle/servico_busca_edita.html', {'title':'Editar Servico', 'servicos':servicos})
            return render(request, 'lavajato_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def salva_servico(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'dayson':
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
                    return render(request, 'lavajato_controle/servico_busca_edita.html', {'title':'Editar Servico', 'servicos':servicos, 'msg':msg})
                return render(request, 'lavajato_controle/servico_busca_edita.html', {'title':'Editar Servico', 'servicos':servicos})
            return render(request, 'lavajato_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def ponto(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'dayson':
            if cargo == 'funcionario':
                if request.method == 'POST' and request.POST.get('entrada') != None:
                    func = request.user.username
                    novo_registro = reg_ponto(estado = 1, operacao = 1, funcionario = func)
                    novo_registro.save()
                    msg = "Ponto registrado com sucesso!"
                    return render(request, 'chica_controle/registro_ponto.html', {'title':'Registro de Ponto', 'msg':msg})
                if request.method == 'POST' and request.POST.get('saida') != None:
                    func = request.user.username
                    novo_registro = reg_ponto(estado = 1, operacao = 2, funcionario = func)
                    novo_registro.save()
                    msg = "Ponto registrado com sucesso!"
                    return render(request, 'lavajato_controle/registro_ponto.html', {'title':'Registro de Ponto', 'msg':msg})
                return render(request, 'lavajato_controle/registro_ponto.html', {'title':'Registro de Ponto'})
            if cargo == 'boss':
                try:
                    pendencias = reg_ponto.objects.filter(estado=1).count()
                except:
                    pendencias = 0
                return render(request, 'lavajato_controle/ponto_boss.html', {'title':'Ponto', 'pendencias':pendencias})
            return render(request, 'lavajato_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def confirma_ponto(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'dayson':
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
                    return render(request, 'lavajato_controle/confirmacao_ponto.html', {'title':'Confirmacao de Ponto', 'ponto_aberto':ponto_aberto, 'msg':msg})
                return render(request, 'lavajato_controle/confirmacao_ponto.html', {'title':'Confirmacao de Ponto', 'ponto_aberto':ponto_aberto})
            return render(request, 'lavajato_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def busca_agendamento(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'dayson':
            if cargo == 'boss':
                hoje = timezone.now()
                agendamentos = agenda.objects.filter(data__date=hoje).order_by('data')
                if request.method == 'GET' and request.GET.get('data') != None:
                    hoje = request.GET.get('data')
                    agendamentos = agenda.objects.filter(data__date=hoje).order_by('data')
                    return render(request, 'lavajato_controle/controle_busca_agendamento.html', {'title':'Buscar Agendamentos', 'agendamentos':agendamentos, 'hoje':hoje})
                if request.method == 'POST' and request.POST.get('agendamento_id') != None:
                    agendamento_id = request.POST.get('agendamento_id')
                    agenda_obj = agenda.objects.get(id=agendamento_id)
                    servicos = agenda_obj.item_servico.all()
                    pagaments = agenda_obj.pag.all()
                    return render(request, 'lavajato_controle/controle_visualizar_agendamento.html', {'title':'Visualizar Agendamento', 'agenda_obj':agenda_obj, 'servicos':servicos, 'pagaments':pagaments})
                return render(request, 'lavajato_controle/controle_busca_agendamento.html', {'title':'Buscar Agendamentos', 'agendamentos':agendamentos, 'hoje':hoje})
            return render(request, 'lavajato_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def info_agendamento(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'dayson':
            if cargo == 'boss':
            
                return render(request, 'lavajato_controle/controle_info_agendamento.html', {'title':'Info Agendamentos'})
            return render(request, 'lavajato_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def nova_senha(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            if request.method == 'GET':
                return render(request, 'lavajato_controle/nova_senha.html', {'title':'Alterar senha'})
            if request.method == 'POST' and request.POST.get('nova_senha') != None and request.POST.get('nova_senha_1') != None:
                nova_senha = request.POST.get('nova_senha')
                nova_senha_1 = request.POST.get('nova_senha_1')
                nome = request.user.username
                usuario = User.objects.get(username__exact=nome)
                if nova_senha == nova_senha_1:
                    usuario.set_password(nova_senha)
                    usuario.save()
                    msg = "Senha alterada com sucesso."
                    return render(request, 'lavajato_controle/home.html', {'title':'Home', 'msg':msg})
                if nova_senha != nova_senha_1:
                    msg = "Senhas incorretas, digite novamente."
                    return render(request, 'lavajato_controle/nova_senha.html', {'title':'Alterar senha', 'msg':msg})
                return render(request, 'lavajato_home/home.html', {'title':'Home'})
            if request.method == 'POST' and request.POST.get('nova_senha') == None or request.POST.get('nova_senha_1') == None:
                msg = "Senhas incorretas, digite novamente."
                return render(request, 'lavajato_controle/nova_senha.html', {'title':'Alterar senha', 'msg':msg})
            return render(request, 'lavajato_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def conta_entrada(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'dayson':
            if cargo == 'boss':
                empresa_obj = conta_empresa.objects.latest('id')
                total_empresa = empresa_obj.total
                if request.method == 'POST' and request.POST.get('desc') != None:
                    desc = request.POST.get('desc')
                    valor = request.POST.get('valor')
                    empresa_obj = conta_empresa.objects.latest('id')
                    ultimo_id = empresa_obj.id
                    ultimo_id = int(ultimo_id) + 1
                    desc = "Entrada - " + desc
                    novo_total = empresa_obj.total + Decimal(valor)
                    nova_entrada = conta_empresa(operacao=1, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                    nova_entrada.save()
                    msg = "Entrada registrada com sucesso!"
                    return render(request, 'lavajato_controle/controle_entrada_conta.html', {'title':'Entrada', 'msg':msg})
                return render(request, 'lavajato_controle/controle_entrada_conta.html', {'title':'Entrada', 'total_empresa':total_empresa})
            return render(request, 'sistema_login/erro.html', {'title':'Erro'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def conta_retirada(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'dayson':
            if cargo == 'boss':
                empresa_obj = conta_empresa.objects.latest('id')
                total_empresa = empresa_obj.total
                if request.method == 'POST' and request.POST.get('desc') != None:
                    desc = request.POST.get('desc')
                    valor = request.POST.get('valor')
                    empresa_obj = conta_empresa.objects.latest('id')
                    ultimo_id = empresa_obj.id
                    ultimo_id = int(ultimo_id) + 1
                    desc = "Retirada - " + desc
                    novo_total = empresa_obj.total - Decimal(valor)
                    nova_saida = conta_empresa(operacao=2, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                    nova_saida.save()
                    msg = "Saida registrada com sucesso!"
                    return render(request, 'lavajato_controle/controle_retirada_conta.html', {'title':'Saida', 'msg':msg})
                return render(request, 'lavajato_controle/controle_retirada_conta.html', {'title':'Retirada da Conta', 'total_empresa':total_empresa})
            return render(request, 'sistema_login/erro.html', {'title':'Erro'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def extrato(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        cargo = request.user.last_name
        if empresa == 'dayson':
            if cargo == 'boss':
                hoje = datetime.now()
                data_inicio = datetime.now().strftime('%Y-%m-%d')
                data_fim = datetime.now() + timedelta(days=-30)
                data_fim = data_fim.strftime('%Y-%m-%d')
                mes = hoje.month
                n_entradas = 0
                n_saidas = 0
                t_entradas = 0
                t_saidas = 0
                conta_all = conta_empresa.objects.filter(data__month=mes).all()
                for a in conta_empresa.objects.filter(operacao=1, data__month=mes).all():
                    t_entradas = t_entradas + a.valor_operacao
                    n_entradas = n_entradas + 1
                for b in conta_empresa.objects.filter(operacao=2, data__month=mes).all():
                    t_saidas = t_saidas + b.valor_operacao
                    n_saidas = n_saidas + 1
                total_geral = t_entradas - t_saidas
                return render(request, 'lavajato_controle/controle_conta_empresa.html', {'title':'Extrato da Conta Empresa', 'data_inicio':data_inicio, 'data_fim':data_fim, 't_saidas':t_saidas, 't_entradas':t_entradas, 'total_geral':total_geral, 'conta_all':conta_all})
            return render(request, 'lavajato_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

