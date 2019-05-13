from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^reg/$', views.reg, name="reg"),
    url(r'^login/$', views.login, name="login"),
    url(r'^list/$', views.list, name="list"),
    # 传统传参
    # url(r'^delete/$', views.delete, name="delete"),
    # 位置传参
    # url(r'(\d+)/delete/$', views.delete, name="delete"),
    # 命名传参  ?代表参数（固定） P大写 代表参数的单词（固定）
    # <>(固定) id（可变）和函数里的参数必须保持一致 \d为正则（可变）
    # 如果是字符串则用\w  命名参数仅此一步
    url(r'(?P<id>\d+)/delete/$', views.delete, name="delete"),
    url(r'update/(?P<id>\d+)/$', views.update, name="update"),
]
