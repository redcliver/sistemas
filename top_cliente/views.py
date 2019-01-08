from django.shortcuts import render
import datetime
from .models import cliente, cliente_portabilidade
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def top_cliente(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'top':
            hoje = datetime.date.today().strftime('%Y-%m-%d')
            if request.method == 'POST' and request.POST.get('nome') != None:
                responsavel = request.user.username
                convenio = request.POST.get('convenio')
                operacao = request.POST.get('operacao')
                banco_cad = request.POST.get('banco_cad')
                cpf = request.POST.get('cpf')
                beneficio = request.POST.get('beneficio')
                uf_beneficio = request.POST.get('uf_beneficio')
                nome = request.POST.get('nome')
                pai = request.POST.get('pai')
                mae = request.POST.get('mae')
                endereco = request.POST.get('endereco')
                numero = request.POST.get('numero')
                bairro = request.POST.get('bairro')
                cep = request.POST.get('cep')
                cidade = request.POST.get('cidade')
                uf_cidade = request.POST.get('uf_cidade')
                data_nasc = request.POST.get('data_nasc')
                natural = request.POST.get('natural')
                uf_natural = request.POST.get('uf_natural')
                rg = request.POST.get('rg')
                expedicao = request.POST.get('expedicao')
                data_exp = request.POST.get('data_exp')
                escolaridade = request.POST.get('escolaridade')
                tel = request.POST.get('tel')
                cel = request.POST.get('cel')
                mail = request.POST.get('mail')
                especie_beneficio = request.POST.get('especie_beneficio')
                renda = request.POST.get('renda')
                cad_senha = request.POST.get('cad_senha')
                senha_econsig = request.POST.get('senha_econsig')
                prec = request.POST.get('prec')
                id_mg = request.POST.get('id_mg')
                valor_solicitado = request.POST.get('valor_solicitado')
                n_parcela = request.POST.get('n_parcela')
                valor_parcela = request.POST.get('valor_parcela')
                f_pagamento = request.POST.get('f_pagamento')
                banco = request.POST.get('banco')
                agencia = request.POST.get('agencia')
                n_conta = request.POST.get('n_conta')
                t_conta = request.POST.get('t_conta')
                obs = request.POST.get('obs')
                novo_cliente = cliente(convenio=convenio, operacao=operacao, banco_cad=banco_cad, cpf = cpf, beneficio=beneficio, uf_beneficio=uf_beneficio, nome=nome, pai=pai, mae = mae, endereco=endereco , numero=numero, bairro=bairro, cep=cep, cidade = cidade, uf_cidade=uf_cidade, data_nasc=data_nasc, natural=natural, uf_natural=uf_natural, rg = rg, expedicao=expedicao, data_exp=data_exp, escolaridade=escolaridade, tel=tel, cel = cel, mail=mail, especie_beneficio=especie_beneficio, renda=renda, cad_senha=cad_senha, senha_econsig = senha_econsig, prec=prec, id_mg=id_mg, valor_solicitado=valor_solicitado, n_parcela=n_parcela, valor_parcela = valor_parcela, f_pagamento=f_pagamento, banco=banco, agencia=agencia, n_conta=n_conta, t_conta = t_conta, obs=obs, responsavel=responsavel)
                novo_cliente.save()
                msg = nome+" salvo com sucesso!"
                return render(request, 'top_cliente/cliente_novo.html', {'title':'Novo Cliente', 'msg':msg})
            return render(request, 'top_cliente/cliente_novo.html', {'title':'Novo Cliente', 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def portabilidade(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'top':
            hoje = datetime.date.today().strftime('%Y-%m-%d')
            if request.method == 'POST' and request.POST.get('nome') != None:
                responsavel = request.user.username
                orgao = request.POST.get('orgao')
                n_beneficio = request.POST.get('n_beneficio')
                especie_beneficio = request.POST.get('especie_beneficio')
                uf_beneficio = request.POST.get('uf_beneficio')
                nome = request.POST.get('nome')
                cpf = request.POST.get('cpf')
                data_nasc = request.POST.get('data_nasc')
                natural = request.POST.get('natural')
                uf_natural = request.POST.get('uf_natural')
                endereco = request.POST.get('endereco')
                numero = request.POST.get('numero')
                bairro = request.POST.get('bairro')
                cep = request.POST.get('cep')
                cidade = request.POST.get('cidade')
                uf_cidade = request.POST.get('uf_cidade')
                tel = request.POST.get('tel')
                cel = request.POST.get('cel')
                mail = request.POST.get('mail')
                banco_atual = request.POST.get('banco_atual')
                banco_portador = request.POST.get('banco_portador')
                ctt = request.POST.get('ctt')
                quitacao = request.POST.get('quitacao')
                valor_parcela = request.POST.get('valor_parcela')
                liquido = request.POST.get('liquido')
                banco_atual1 = request.POST.get('banco_atual1')
                banco_portador1 = request.POST.get('banco_portador1')
                ctt1 = request.POST.get('ctt1')
                quitacao1 = request.POST.get('quitacao1')
                valor_parcela1 = request.POST.get('valor_parcela1')
                liquido1 = request.POST.get('liquido1')
                banco_atual2 = request.POST.get('banco_atual2')
                banco_portador2 = request.POST.get('banco_portador2')
                ctt2 = request.POST.get('ctt')
                quitacao2 = request.POST.get('quitacao2')
                valor_parcela2 = request.POST.get('valor_parcela2')
                liquido2 = request.POST.get('liquido2')
                banco_atual3 = request.POST.get('banco_atual3')
                banco_portador3 = request.POST.get('banco_portador3')
                ctt3 = request.POST.get('ctt3')
                quitacao3 = request.POST.get('quitacao3')
                valor_parcela3 = request.POST.get('valor_parcela3')
                liquido3 = request.POST.get('liquido3')
                f_pagamento = request.POST.get('f_pagamento')
                banco = request.POST.get('banco')
                agencia = request.POST.get('agencia')
                n_conta = request.POST.get('n_conta')
                t_conta = request.POST.get('t_conta')
                obs = request.POST.get('obs')
                novo_cliente_portabilidade = cliente_portabilidade(orgao=orgao, n_beneficio=n_beneficio, especie_beneficio=especie_beneficio, uf_beneficio = uf_beneficio, nome=nome, cpf=cpf, data_nasc=data_nasc, natural=natural, uf_natural = uf_natural, endereco=endereco , numero=numero, bairro=bairro, cep=cep, cidade = cidade, uf_cidade=uf_cidade, banco_atual=banco_atual, banco_portador=banco_portador, ctt=ctt, quitacao = quitacao, valor_parcela=valor_parcela, liquido=liquido, banco_atual1=banco_atual1, banco_portador1=banco_portador1, ctt1=ctt1, quitacao1 = quitacao1, valor_parcela1=valor_parcela1, liquido1=liquido1, banco_atual2=banco_atual2, banco_portador2=banco_portador2, ctt2=ctt2, quitacao2 = quitacao2, valor_parcela2=valor_parcela2, liquido2=liquido2, banco_atual3=banco_atual3, banco_portador3=banco_portador3, ctt3=ctt3, quitacao3 = quitacao3, valor_parcela3=valor_parcela3, liquido3=liquido3, tel=tel, cel = cel, mail=mail, f_pagamento=f_pagamento, banco=banco, agencia=agencia, n_conta=n_conta, t_conta = t_conta, obs=obs, responsavel=responsavel)
                novo_cliente_portabilidade.save()
                msg = nome+" salvo com sucesso!"
                return render(request, 'top_cliente/cliente_novo_portabilidade.html', {'title':'Novo Cliente Portabilidade', 'msg':msg})
            return render(request, 'top_cliente/cliente_novo_portabilidade.html', {'title':'Novo Cliente Portabilidade', 'hoje':hoje})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def busca(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'top':
            clientes = cliente.objects.all().order_by('nome')
            clientes_port = cliente_portabilidade.objects.all().order_by('nome')
            return render(request, 'top_cliente/cliente_busca.html', {'title':'Buscar Cliente ', 'clientes':clientes, 'clientes_port':clientes_port})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def visualiza(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'top':
            clientes = cliente.objects.all().order_by('nome')
            clientes_port = cliente_portabilidade.objects.all().order_by('nome')
            if request.method == 'GET' and request.GET.get('cliente_id') != "Nulo" and request.GET.get('cliente_id_portabilidade') == "Nulo":
                cliente_id = request.GET.get('cliente_id')
                cliente_obj = cliente.objects.get(id=cliente_id)
                return render(request, 'top_cliente/cliente_visualizar.html', {'title':'Visualizar Cliente', 'cliente_obj':cliente_obj})
            if request.method == 'POST' and request.POST.get('cliente_id') != "Nulo" and request.POST.get('cliente_id_portabilidade') == "Nulo":
                cliente_id = request.POST.get('cliente_id')
                cliente_obj = cliente.objects.get(id=cliente_id)
                return render(request, 'top_cliente/cliente_edita.html', {'title':'Editar Cliente', 'cliente_obj':cliente_obj})
            if request.method == 'GET' and request.GET.get('cliente_id') == "Nulo" and request.GET.get('cliente_id_portabilidade') != "Nulo":
                cliente_id_portabilidade = request.GET.get('cliente_id_portabilidade')
                cliente_obj_port = cliente_portabilidade.objects.get(id=cliente_id_portabilidade)
                return render(request, 'top_cliente/cliente_visualizar_portabilidade.html', {'title':'Visualizar Cliente', 'cliente_obj_port':cliente_obj_port})
            if request.method == 'POST' and request.POST.get('cliente_id') == None and request.POST.get('cliente_id_portabilidade') != None:
                cliente_id_portabilidade = request.POST.get('cliente_id_portabilidade')
                cliente_obj_port = cliente_portabilidade.objects.get(id=cliente_id_portabilidade)
                return render(request, 'top_cliente/cliente_edita_portabilidade.html', {'title':'Editar Cliente', 'cliente_obj_port':cliente_obj_port})
            return render(request, 'top_cliente/cliente_busca.html', {'title':'Buscar Cliente ', 'clientes':clientes, 'clientes_port':clientes_port})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def edita(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'top':
            clientes = cliente.objects.all().order_by('nome')
            clientes_port = cliente_portabilidade.objects.all().order_by('nome')
            if request.method == 'GET' and request.GET.get('cliente_id') != None:
                cliente_id = request.GET.get('cliente_id')
                cliente_obj = cliente.objects.get(id=cliente_id)
                return render(request, 'top_cliente/cliente_edita.html', {'title':'Editar Cliente', 'cliente_obj':cliente_obj})
            if request.method == 'POST' and request.POST.get('cliente_id') != None:
                cliente_id = request.POST.get('cliente_id')
                cliente_obj = cliente.objects.get(id=cliente_id)
                convenio = request.POST.get('convenio')
                operacao = request.POST.get('operacao')
                banco_cad = request.POST.get('banco_cad')
                cpf = request.POST.get('cpf')
                beneficio = request.POST.get('beneficio')
                uf_beneficio = request.POST.get('uf_beneficio')
                nome = request.POST.get('nome')
                pai = request.POST.get('pai')
                mae = request.POST.get('mae')
                endereco = request.POST.get('endereco')
                numero = request.POST.get('numero')
                bairro = request.POST.get('bairro')
                cep = request.POST.get('cep')
                cidade = request.POST.get('cidade')
                uf_cidade = request.POST.get('uf_cidade')
                data_nasc = request.POST.get('data_nasc')
                natural = request.POST.get('natural')
                uf_natural = request.POST.get('uf_natural')
                rg = request.POST.get('rg')
                expedicao = request.POST.get('expedicao')
                data_exp = request.POST.get('data_exp')
                escolaridade = request.POST.get('escolaridade')
                tel = request.POST.get('tel')
                cel = request.POST.get('cel')
                mail = request.POST.get('mail')
                especie_beneficio = request.POST.get('especie_beneficio')
                renda = request.POST.get('renda')
                cad_senha = request.POST.get('cad_senha')
                senha_econsig = request.POST.get('senha_econsig')
                prec = request.POST.get('prec')
                id_mg = request.POST.get('id_mg')
                valor_solicitado = request.POST.get('valor_solicitado')
                n_parcela = request.POST.get('n_parcela')
                valor_parcela = request.POST.get('valor_parcela')
                f_pagamento = request.POST.get('f_pagamento')
                banco = request.POST.get('banco')
                agencia = request.POST.get('agencia')
                n_conta = request.POST.get('n_conta')
                t_conta = request.POST.get('t_conta')
                obs = request.POST.get('obs')
                cliente_obj.convenio = convenio
                cliente_obj.operacao = operacao
                cliente_obj.banco_cad = banco_cad
                cliente_obj.cpf = cpf
                cliente_obj.beneficio = beneficio
                cliente_obj.uf_beneficio = uf_beneficio
                cliente_obj.nome = nome
                cliente_obj.pai = pai
                cliente_obj.mae = mae
                cliente_obj.endereco = endereco
                cliente_obj.numero = numero
                cliente_obj.bairro = bairro
                cliente_obj.cep = cep
                cliente_obj.cidade = cidade
                cliente_obj.uf_cidade = uf_cidade
                cliente_obj.data_nasc = data_nasc
                cliente_obj.natural =natural
                cliente_obj.uf_natural = uf_natural
                cliente_obj.rg = rg
                cliente_obj.expedicao = expedicao
                cliente_obj.data_exp = data_exp
                cliente_obj.escolaridade = escolaridade
                cliente_obj.tel = tel
                cliente_obj.cel = cel 
                cliente_obj.mail = mail
                cliente_obj.especie_beneficio = especie_beneficio
                cliente_obj.renda = renda
                cliente_obj.cad_senha = cad_senha
                cliente_obj.senha_econsig = senha_econsig
                cliente_obj.prec = prec
                cliente_obj.id_mg = id_mg
                cliente_obj.valor_solicitado = valor_solicitado
                cliente_obj.f_pagamento = f_pagamento
                cliente_obj.banco = banco
                cliente_obj.agencia = agencia
                cliente_obj.n_conta = n_conta
                cliente_obj.t_conta = t_conta
                cliente_obj.save()
                return render(request, 'top_cliente/cliente_visualizar.html', {'title':'Visualiza Cliente', 'cliente_obj':cliente_obj})
            if request.method == 'GET' and request.GET.get('cliente_id_portabilidade') != None:
                cliente_id_portabilidade = request.GET.get('cliente_id_portabilidade')
                cliente_obj_port = cliente_portabilidade.objects.get(id=cliente_id_portabilidade)
                return render(request, 'top_cliente/cliente_edita_portabilidade.html', {'title':'Editar Cliente', 'cliente_obj_port':cliente_obj_port})
            if request.method == 'POST' and request.POST.get('nome') != None:
                cliente_id_portabilidade = request.POST.get('cliente_id_portabilidade')
                cliente_obj_port = cliente_portabilidade.objects.get(id=cliente_id_portabilidade)
                orgao = request.POST.get('orgao')
                n_beneficio = request.POST.get('n_beneficio')
                especie_beneficio = request.POST.get('especie_beneficio')
                uf_beneficio = request.POST.get('uf_beneficio')
                nome = request.POST.get('nome')
                cpf = request.POST.get('cpf')
                data_nasc = request.POST.get('data_nasc')
                natural = request.POST.get('natural')
                uf_natural = request.POST.get('uf_natural')
                endereco = request.POST.get('endereco')
                numero = request.POST.get('numero')
                bairro = request.POST.get('bairro')
                cep = request.POST.get('cep')
                cidade = request.POST.get('cidade')
                uf_cidade = request.POST.get('uf_cidade')
                tel = request.POST.get('tel')
                cel = request.POST.get('cel')
                mail = request.POST.get('mail')
                banco_atual = request.POST.get('banco_atual')
                banco_portador = request.POST.get('banco_portador')
                ctt = request.POST.get('ctt')
                quitacao = request.POST.get('quitacao')
                valor_parcela = request.POST.get('valor_parcela')
                liquido = request.POST.get('liquido')
                banco_atual1 = request.POST.get('banco_atual1')
                banco_portador1 = request.POST.get('banco_portador1')
                ctt1 = request.POST.get('ctt1')
                quitacao1 = request.POST.get('quitacao1')
                valor_parcela1 = request.POST.get('valor_parcela1')
                liquido1 = request.POST.get('liquido1')
                banco_atual2 = request.POST.get('banco_atual2')
                banco_portador2 = request.POST.get('banco_portador2')
                ctt2 = request.POST.get('ctt')
                quitacao2 = request.POST.get('quitacao2')
                valor_parcela2 = request.POST.get('valor_parcela2')
                liquido2 = request.POST.get('liquido2')
                banco_atual3 = request.POST.get('banco_atual3')
                banco_portador3 = request.POST.get('banco_portador3')
                ctt3 = request.POST.get('ctt3')
                quitacao3 = request.POST.get('quitacao3')
                valor_parcela3 = request.POST.get('valor_parcela3')
                liquido3 = request.POST.get('liquido3')
                f_pagamento = request.POST.get('f_pagamento')
                banco = request.POST.get('banco')
                agencia = request.POST.get('agencia')
                n_conta = request.POST.get('n_conta')
                t_conta = request.POST.get('t_conta')
                obs = request.POST.get('obs')
                cliente_obj_port.orgao = orgao
                cliente_obj_port.n_beneficio = n_beneficio
                cliente_obj_port.especie_beneficio = especie_beneficio
                cliente_obj_port.uf_beneficio = uf_beneficio
                cliente_obj_port.nome = nome
                cliente_obj_port.cpf = cpf
                cliente_obj_port.data_nasc = data_nasc
                cliente_obj_port.natural = natural
                cliente_obj_port.uf_natural = uf_natural
                cliente_obj_port.endereco = endereco
                cliente_obj_port.numero = numero
                cliente_obj_port.bairro = bairro
                cliente_obj_port.cep = cep
                cliente_obj_port.cidade = cidade
                cliente_obj_port.uf_cidade = uf_cidade
                cliente_obj_port.tel = tel
                cliente_obj_port.cel = cel
                cliente_obj_port.mail = mail
                cliente_obj_port.banco_atual = banco_atual
                cliente_obj_port.banco_portador = banco_portador
                cliente_obj_port.ctt = ctt
                cliente_obj_port.quitacao = quitacao
                cliente_obj_port.valor_parcela = valor_parcela
                cliente_obj_port.liquido = liquido
                cliente_obj_port.banco_atual1 = banco_atual1
                cliente_obj_port.banco_portador1 = banco_portador1
                cliente_obj_port.ctt1 = ctt1
                cliente_obj_port.quitacao1 = quitacao1
                cliente_obj_port.valor_parcela1 = valor_parcela1
                cliente_obj_port.liquido1 = liquido1
                cliente_obj_port.banco_atual2 = banco_atual2
                cliente_obj_port.banco_portador2 = banco_portador2
                cliente_obj_port.ctt2 = ctt2
                cliente_obj_port.quitacao2 = quitacao2
                cliente_obj_port.valor_parcela2 = valor_parcela2
                cliente_obj_port.liquido2 = liquido2
                cliente_obj_port.banco_atual3 = banco_atual3
                cliente_obj_port.banco_portador3 = banco_portador3
                cliente_obj_port.ctt3 = ctt3
                cliente_obj_port.quitacao3 = quitacao3
                cliente_obj_port.valor_parcela3 = valor_parcela3
                cliente_obj_port.liquido3 = liquido3
                cliente_obj_port.f_pagamento = f_pagamento
                cliente_obj_port.banco = banco
                cliente_obj_port.agencia = agencia
                cliente_obj_port.n_conta = n_conta
                cliente_obj_port.t_conta = t_conta
                cliente_obj_port.obs = obs
                cliente_obj_port.save()
                return render(request, 'top_cliente/cliente_visualizar_portabilidade.html', {'title':'Visualiza Cliente', 'cliente_obj_port':cliente_obj_port})
            return render(request, 'top_cliente/cliente_busca.html', {'title':'Buscar Cliente ', 'clientes':clientes, 'clientes_port':clientes_port})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})


def contrato_busca(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'top':
            clientes = cliente.objects.all().order_by('nome')
            clientes_port = cliente_portabilidade.objects.all().order_by('nome')
            return render(request, 'top_cliente/cliente_contrato_busca.html', {'title':'Imprimir Contrato ', 'clientes':clientes, 'clientes_port':clientes_port})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf.html')
        if request.method == 'GET' and request.GET.get('cliente_id') != "Nulo" and request.GET.get('cliente_id_portabilidade') == "Nulo":
            cliente_id = request.GET.get('cliente_id')
            cliente_obj = cliente.objects.get(id=cliente_id)

            context = {
                    "convenio": cliente_obj.get_convenio_display,
                    "operacao": cliente_obj.operacao,
                    "data_cadastro": cliente_obj.data_cadastro.strftime('%d/%m/%Y'),
                    "banco_cad": cliente_obj.banco_cad,
                    "cpf": cliente_obj.cpf,
                    "beneficio": cliente_obj.beneficio,
                    "uf_beneficio": cliente_obj.uf_beneficio,
                    "nome": cliente_obj.nome,
                    "pai": cliente_obj.pai,
                    "mae": cliente_obj.mae,
                    "endereco": cliente_obj.endereco,
                    "numero": cliente_obj.numero,
                    "bairro": cliente_obj.bairro,
                    "cep": cliente_obj.cep,
                    "cidade": cliente_obj.cidade,
                    "uf_cidade": cliente_obj.uf_cidade,
                    "data_nasc": cliente_obj.data_nasc.strftime('%d/%m/%Y'),
                    "natural": cliente_obj.natural,
                    "uf_natural": cliente_obj.uf_natural,
                    "rg": cliente_obj.rg,
                    "exp": cliente_obj.expedicao,
                    "data_exp": cliente_obj.data_exp.strftime('%d/%m/%Y'),
                    "escolaridade": cliente_obj.escolaridade,
                    "tel": cliente_obj.tel,
                    "cel": cliente_obj.cel,
                    "mail": cliente_obj.mail,
                    "especie_beneficio": cliente_obj.especie_beneficio,
                    "renda": cliente_obj.renda,
                    "cad_senha": cliente_obj.cad_senha,
                    "senha_econsig": cliente_obj.senha_econsig,
                    "prec": cliente_obj.prec,
                    "id_mg": cliente_obj.id_mg,
                    "valor_solicitado": cliente_obj.valor_solicitado,
                    "n_parcela": cliente_obj.n_parcela,
                    "valor_parcela": cliente_obj.valor_parcela,
                    "f_pagamento": cliente_obj.f_pagamento,
                    "banco": cliente_obj.banco,
                    "agencia": cliente_obj.agencia,
                    "n_conta": cliente_obj.n_conta,
                    "t_conta": cliente_obj.t_conta,
                    "responsavel": cliente_obj.responsavel,
                }
            html = template.render(context)
            pdf = render_to_pdf('pdf.html', context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "Ficha_%s.pdf" %(cliente_obj.nome)
                content = "inline-block; filename='%s'" %(filename)
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename='%s'" %(filename)
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")
        return HttpResponse(pdf, content_type='application/pdf')