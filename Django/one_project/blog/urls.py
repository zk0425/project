from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^log/$', views.log, name="log"),
    url(r'^reg/$', views.reg, name="reg")
]