from django.shortcuts import render
from .models import produto, lote
from decimal import Decimal

# Create your views here.
def entrada(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            produtos = produto.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('produto_id') != None:
                produto_id = request.POST.get('produto_id')
                produto_obj = produto.objects.filter(id=produto_id).get()
                return render(request, 'chica_estoque/estoque_entrada.html', {'title':'Entrada de estoque', 'produto_obj':produto_obj})
            return render(request, 'chica_estoque/estoque_entrada.html', {'title':'Entrada de estoque', 'produtos':produtos})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def nova_entrada(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            produtos = produto.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('novo_lote') != None:
                produto_id = request.POST.get('novo_lote')
                produto_obj = produto.objects.filter(id=produto_id).get()
                valor_compra = request.POST.get('valor_compra')
                valor_venda = request.POST.get('valor_venda')
                quantidade = request.POST.get('quantidade')
                n_lote = lote(prod=produto_obj, valor_compra=valor_compra, valor_venda=valor_venda, quantidade=quantidade)
                n_lote.save()
                produto_obj.quantidade = produto_obj.quantidade + Decimal(quantidade)
                produto_obj.valor_compra = valor_compra
                produto_obj.valor_venda = valor_venda
                lucro = Decimal(valor_compra) - Decimal(valor_venda)
                lucro = lucro / Decimal(valor_compra)
                lucro = lucro * 100
                lucro = abs(lucro)
                produto_obj.lucro = lucro
                produto_obj.save()
                msg = produto_obj.nome + " adicionado com sucesso ao estoque."
                return render(request, 'chica_estoque/estoque_entrada.html', {'title':'Entrada de estoque', 'msg':msg})
            return render(request, 'chica_estoque/estoque_entrada.html', {'title':'Entrada de estoque', 'produtos':produtos})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def novo_produto(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            if request.method == 'POST' and request.POST.get('nome') != None:
                nome = request.POST.get('nome')
                valor_compra = request.POST.get('valor_compra')
                valor_venda = request.POST.get('valor_venda')
                quantidade = request.POST.get('quantidade')
                quantidade_minima = request.POST.get('quantidade_minima')
                lucro = Decimal(valor_compra) - Decimal(valor_venda)
                lucro = lucro / Decimal(valor_compra)
                lucro = lucro * 100
                lucro = lucro * -1
                novo_produto = produto(nome=nome, valor_compra=valor_compra, valor_venda=valor_venda, quantidade=quantidade, quantidade_minima=quantidade_minima, lucro=lucro)
                novo_produto.save()
                msg = novo_produto.nome + " cadastrado com suceso!"
                return render(request, 'chica_estoque/estoque_produto.html', {'title':'Novo Produto', 'msg':msg})
            return render(request, 'chica_estoque/estoque_produto.html', {'title':'Novo Produto'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def consulta(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            produtos = produto.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('produto_id') != None:
                produto_id = request.POST.get('produto_id')
                produto_obj = produto.objects.filter(id=produto_id).get()
                return render(request, 'chica_estoque/estoque_consulta.html', {'title':'Consultar estoque', 'produto_obj':produto_obj})
            return render(request, 'chica_estoque/estoque_consulta.html', {'title':'Consultar estoque', 'produtos':produtos})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def saida(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            produtos = produto.objects.all().order_by('nome')
            if request.method == 'POST' and request.POST.get('produto_id') != None:
                produto_id = request.POST.get('produto_id')
                produto_obj = produto.objects.filter(id=produto_id).get()
                return render(request, 'chica_estoque/estoque_consulta.html', {'title':'Saida estoque', 'produto_obj':produto_obj})
            return render(request, 'chica_estoque/estoque_saida.html', {'title':'Saida estoque', 'produtos':produtos})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})