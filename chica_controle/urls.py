from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.chica_controle),
    url(r'^novo_funcionario', views.novo_funcionario),
    url(r'^busca_funcionario', views.busca_funcionario),
    url(r'^edita_funcionario', views.edita_funcionario),
    url(r'^salva_funcionario', views.salva_funcionario),
    url(r'^novo_servico', views.novo_servico),
    url(r'^busca_servico', views.busca_servico),
    url(r'^edita_servico', views.edita_servico),
    url(r'^salva_servico', views.salva_servico),
    url(r'^ponto', views.ponto),
    url(r'^confirma_ponto', views.confirma_ponto),
    url(r'^busca_agendamento', views.busca_agendamento),
    ]
