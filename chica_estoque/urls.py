from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^entrada', views.entrada),
    url(r'^nova_entrada', views.nova_entrada),
    url(r'^novo_produto', views.novo_produto),
    url(r'^consulta', views.consulta),
    ]
