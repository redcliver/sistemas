from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.lavajato_contas),
    url(r'^busca', views.busca),
    url(r'^edita', views.edita),
    url(r'^salva', views.salva),
    url(r'^pagar', views.pagar),
    url(r'^pagamento_gerencia', views.pagamento_gerencia),
    url(r'^pagamento_caixa', views.pagamento_caixa),
    url(r'^conta_receber', views.conta_receber),
    url(r'^confirmar_recebimento', views.confirmar_recebimento),
    url(r'^relatorio', views.relatorio_pagar),
    url(r'^receber', views.receber),
    url(r'^excluir', views.excluir),
    ]
