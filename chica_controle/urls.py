from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.chica_controle),
    url(r'^novo_funcionario', views.novo_funcionario),
    url(r'^busca_funcionario', views.busca_funcionario),
    url(r'^edita_funcionario', views.edita_funcionario),
    url(r'^salva_funcionario', views.salva_funcionario),
    ]
