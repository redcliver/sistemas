from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.lavajato_cliente),
    url(r'^busca', views.busca),
    url(r'^edita', views.edita),
    url(r'^salva', views.salva),
    url(r'^novo_carro', views.novo_carro),
    url(r'^carro_edita', views.carro_edita),
    url(r'^carro_salva_edita', views.carro_salva_edita),
    url(r'^fechamento_mensal', views.fechamento_mensal),
    url(r'^pagamento_geral', views.pagamento_geral),
    url(r'^receber_mensal', views.receber_mensal),
    url(r'^bloqueados', views.bloqueados),
    url(r'^pagar_mes', views.pagar_mes),
    url(r'^informacao', views.informacao),
    url(r'^mes_informacao', views.mes_informacao),
    ]
