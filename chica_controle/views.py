from django.shortcuts import render

# Create your views here.
def chica_controle(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            return render(request, 'chica_controle/controle.html', {'title':'Controle'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})