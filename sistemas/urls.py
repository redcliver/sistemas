"""
Definition of urls for sistemas.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.contrib.auth.views import login

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Sistema
    url(r'^$', login, {'template_name': 'sistema_login/login.html'}),
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

    # URL Mario Miazaky
    url(r'^mario_home/', include('mario_home.urls')),
    url(r'^mario_cliente/', include('mario_cliente.urls')),

    # Padrao
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
]
