from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>网站首页</h1>")


def log(request):
    return HttpResponse("<h1>登录页面</h1>")


def reg(request):
    return HttpResponse("<h1>注册页面</h1>")

