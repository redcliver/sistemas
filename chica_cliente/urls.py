from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.chica_cliente),
    url(r'^busca', views.busca),
    url(r'^edita', views.edita),
    url(r'^salva', views.salva),
    ]
