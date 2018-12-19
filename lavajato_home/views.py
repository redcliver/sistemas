from django.shortcuts import render
from lavajato_contas.models import conta
from django.utils import timezone
import datetime

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            hoje = datetime.date.today().strftime('%Y-%m-%d')
            vencimento_conta = conta.objects.filter(data_pagamento__icontains=hoje, estado = 1).count()
            return render(request, 'lavajato_home/home.html', {'title':'Home', 'vencimento_conta':vencimento_conta})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def suporte(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'dayson':
            return render(request, 'lavajato_home/suporte.html', {'title':'Suporte'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})