from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.lavajato_controle),
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
    url(r'^info_agendamento', views.info_agendamento),
    url(r'^nova_senha', views.nova_senha),
    url(r'^extrato', views.extrato),
    url(r'^conta_entrada', views.conta_entrada),
    url(r'^conta_retirada', views.conta_retirada),
    url(r'^taxa_debito', views.taxa_debito),
    url(r'^taxa_credito_vista', views.taxa_credito_vista),
    url(r'^taxa_credito_prazo', views.taxa_credito_prazo),
    url(r'^taxa_elo_debito', views.taxa_elo_debito),
    url(r'^taxa_credito_elo', views.taxa_credito_elo),
    url(r'^taxa_boleto', views.taxa_boleto),
    ]
