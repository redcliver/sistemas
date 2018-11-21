from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^entrada', views.entrada),
    url(r'^novo_produto', views.novo_produto),
    ]
