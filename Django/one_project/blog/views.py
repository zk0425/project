from django.http import HttpResponse
from . import models


def index(request):
    return HttpResponse("<h1>子模块首页</h1>")


def log(request):
    return HttpResponse("<h1>子模块登录页面</h1>")


def reg(request):
    username = "王五"
    password = "123456"
    try:
        # 第一种  管理器
        # user = models.User.create_user(username=username, password=password)
        # 第二种   类方法
        # user = models.User(username=username, password=password)
        # 第三种   对象属性
        user = models.User.userManager.add_user(username=username, password=password)
        user.save()
        return HttpResponse("<h1>注册成功</h1>")
    except Exception as e:
        print("发生错误，错误信息", e)
        return HttpResponse("<h1>注册失败</h1>")
