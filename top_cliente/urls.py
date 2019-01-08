from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.top_cliente),
    url(r'^portabilidade', views.portabilidade),
    url(r'^busca', views.busca),
    url(r'^visualiza', views.visualiza),
    url(r'^edita', views.edita),
    url(r'^contrato_busca', views.contrato_busca),
    url(r'^imprimir', views.GeneratePdf.as_view()),
    ]
