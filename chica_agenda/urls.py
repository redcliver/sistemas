from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.novo),
    url(r'^edita', views.edita),
    url(r'^visualiza', views.visualiza),
    ]
