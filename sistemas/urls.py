"""
Definition of urls for sistemas.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.contrib.auth.views import LoginView, LogoutView

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Sistema
    url(r'^$', LoginView.as_view(template_name='sistema_login/login.html'), name="login"),
    url(r'^sistema_login/', include('sistema_login.urls')),

    # URL Chica Diniz
    url(r'^chica_home/', include('chica_home.urls')),
    url(r'^chica_cliente/', include('chica_cliente.urls')),
    url(r'^chica_conta/', include('chica_conta.urls')),
    url(r'^chica_controle/', include('chica_controle.urls')),
    url(r'^chica_caixa/', include('chica_caixa.urls')),
    url(r'^chica_estoque/', include('chica_estoque.urls')),
    url(r'^chica_agenda/', include('chica_agenda.urls')),

    # URL Dayson Lava-jato
    url(r'^lavajato_home/', include('lavajato_home.urls')),
    url(r'^lavajato_cliente/', include('lavajato_cliente.urls')),
    url(r'^lavajato_contas/', include('lavajato_contas.urls')),
    url(r'^lavajato_controle/', include('lavajato_controle.urls')),
    url(r'^lavajato_caixa/', include('lavajato_caixa.urls')),
    url(r'^lavajato_estoque/', include('lavajato_estoque.urls')),
    url(r'^lavajato_agenda/', include('lavajato_agenda.urls')),
    url(r'^lavajato_fornecedor/', include('lavajato_fornecedor.urls')),

    # URL Mario Miazaky
    url(r'^mario_home/', include('mario_home.urls')),
    url(r'^mario_cliente/', include('mario_cliente.urls')),

    # URL Chica Diniz
    url(r'^top_home/', include('top_home.urls')),
    url(r'^top_cliente/', include('top_cliente.urls')),

    # Padrao
    url(r'^logout$', LogoutView.as_view(template_name='sistema_login/login.html'), name="login"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin
    url(r'^admin/', admin.site.urls),
]
