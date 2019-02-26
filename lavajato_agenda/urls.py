from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.novo),
    url(r'^edita', views.edita),
    url(r'^salvar', views.salvar),
    url(r'^excluir', views.excluir),
    url(r'^busca', views.busca),
    url(r'^add_servico', views.add_servico),
    url(r'^visualiza', views.visualiza),
    url(r'^ver', views.ver),
    url(r'^checklist', views.checklist),
    url(r'^confirmacao', views.confirmacao),
    url(r'^desconto', views.desconto),
    url(r'^desmarcar', views.desmarcar),
    url(r'^dinheiro', views.dinheiro),
    url(r'^credito', views.credito),
    url(r'^debito', views.debito),
    url(r'^elo_debito', views.elo_debito),
    url(r'^elo_credito', views.elo_credito),
    url(r'^boleto', views.boleto),
    url(r'^add_prazo', views.add_prazo),
    url(r'^agenda_ultima_ordem', views.agenda_ultima_ordem),
    url(r'^ordem_branco', views.ordem_branco),
    url(r'^pag_vencidos', views.pag_vencidos),
    ]
