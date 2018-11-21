from django.shortcuts import render
# Create your views here.
def sistema_login(request):
    if request.user.is_authenticated():
        empresa = request.user.get_short_name()
        if empresa == 'chicadiniz':
            return render(request, 'chica_home/home.html', {'title':'Home'})
        elif empresa == 'dayson':
            return render(request, 'lavajato_home/home.html', {'title':'Home'})
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
    else:
        return render(request, 'sistema_login/erro.html', {'title':'Erro'})
