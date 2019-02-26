from django.shortcuts import render
from django.shortcuts import render
from lavajato_contas.models import conta
from lavajato_estoque.models import produto
from lavajato_agenda.models import parcela, agenda
from lavajato_caixa.models import caixa_geral
from lavajato_controle.models import conta_empresa
from lavajato_cliente.models import cliente
from django.utils import timezone
import datetime
from datetime import datetime
from datetime import timedelta, date
from decimal import Decimal

# Create your views here.
def sistema_login(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            return render(request, 'chica_home/home.html', {'title':'Home'})
        elif empresa == 'dayson':
            data = datetime.now() + timezone.timedelta(days=1)
            for z in parcela.objects.filter(data__lte=data, estado=1).all():
                z.estado = 2
                z.save()
                conta_empresa_obj = conta_empresa.objects.latest('id')
                ultimo_id = z.id
                novo_total = conta_empresa_obj.total + z.valor
                valor = z.valor
                desc = "Parcela : " + str(z.id)
                nova_entrada = conta_empresa(operacao=1, id_operacao=ultimo_id, valor_operacao=valor, descricao=desc, total=novo_total)
                nova_entrada.save()
            dia = datetime.now().strftime('%d')
            mes = datetime.now().strftime('%m')
            bloqueio = datetime.now() + timezone.timedelta(days=-45)
            bloqueio = bloqueio.strftime('%Y-%m-%d')
            bloqueados = 0
            blacklist = None
            boleto = 0
            mes_passado = timezone.now() + timezone.timedelta(days=-30)
            seis_meses = timezone.now() + timezone.timedelta(days=-150)
            try:
                conta_geral = conta_empresa.objects.latest('id')
            except:
                conta_geral = conta_empresa(operacao=1, id_operacao=1, valor_operacao=0, descricao="Abertura", total=0)
                conta_geral.save()
            try:
                caixa = caixa_geral.objects.latest('id')
            except:
                caixa = caixa_geral(operacao=1, id_operacao=1, valor_operacao=0, descricao="Abertura", total=0)
                caixa.save()
            vencimento_conta = 0
            estoque_min = 0
            pag_vencidos = 0
            for a in conta.objects.filter(estado=1, data_venc__lte=data).all():
                vencimento_conta = vencimento_conta + 1
            for b in produto.objects.all():
                if b.quantidade <= b.quantidade_minima or b.quantidade == b.quantidade_minima:
                    estoque_min = estoque_min + 1
            for c in agenda.objects.filter(data__lte=bloqueio, estado=1).all():
                cli_id = c.cli.id
                cli_obj = cliente.objects.filter(id=cli_id).get()
                cli_obj.liberacao = 2
                cli_obj.save()
                bloqueados = bloqueados + 1
            for d in agenda.objects.filter(boleto__lte=data, estado=1):
                boleto = boleto + 1
            for e in agenda.objects.filter(data_pagamento__lte=data, estado=1):
                pag_vencidos = pag_vencidos + 1
            cli_inativo = cliente.objects.all()
            cli_ina_meses = cliente.objects.all()
            for f in agenda.objects.filter(data__gte=seis_meses).all():
                cli_ina_meses = cli_ina_meses.exclude(id=f.cli.id)
                if f.data >= mes_passado:
                    cli_inativo = cli_inativo.exclude(id=f.cli.id)
            aniversario = cliente.objects.filter(data_nasc__day=dia, data_nasc__month=mes).all()
            return render(request, 'lavajato_home/home.html', {'title':'Home','pag_vencidos':pag_vencidos, 'boleto':boleto, 'bloqueados':bloqueados, 'aniversario':aniversario, 'vencimento_conta':vencimento_conta, 'estoque_min':estoque_min, 'cli_inativo':cli_inativo, 'cli_ina_meses':cli_ina_meses})
        elif empresa == 'mario':
            return render(request, 'mario_home/home.html', {'title':'Home'})
        elif empresa == 'top':
            return render(request, 'top_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
