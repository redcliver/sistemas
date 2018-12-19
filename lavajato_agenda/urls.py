from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.novo),
    url(r'^edita', views.edita),
    url(r'^excluir', views.excluir),
    url(r'^busca', views.busca),
    url(r'^add_servico', views.add_servico),
    url(r'^visualiza', views.visualiza),
    url(r'^confirmacao', views.confirmacao),
    url(r'^desmarcar', views.desmarcar),
    url(r'^dinheiro', views.dinheiro),
    url(r'^credito', views.credito),
    url(r'^debito', views.debito),
    ]
