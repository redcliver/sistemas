from django.shortcuts import render

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'mario':
            return render(request, 'mario_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})

def suporte(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'mario':
            return render(request, 'mario_home/suporte.html', {'title':'Suporte'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})