from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.lavajato_cliente),
    url(r'^busca', views.busca),
    url(r'^edita', views.edita),
    url(r'^salva', views.salva),
    url(r'^novo_carro', views.novo_carro),
    url(r'^edita_carro', views.edita_carro),
    url(r'^salva_edita_carro', views.salva_edita_carro),
    ]
