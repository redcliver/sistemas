from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.lavajato_caixa),
    url(r'^entrada', views.entrada),
    url(r'^saida', views.saida),
    url(r'^conferencia', views.conferencia),
    url(r'^fechar', views.fechar),
    ]
