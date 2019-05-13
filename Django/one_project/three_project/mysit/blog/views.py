# from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
# def index(requser):
#     return HttpResponse('项目首页面')
#
#
# def login(requser):
#     return HttpResponse('登录页面')
#
#
# def reg(requser):
#     return HttpResponse('注册页面')


def index(request):
    return render(request, "blog/index.html", {"msg": "请认真填写以下选项："})

def reg(request):
    # 传递参数
    if request.method == "GET":
        return render(request, 'blog/reg.html', {})
    else:
        name = request.POST["name"].strip()
        password = request.POST["password"].strip()
        password2 = request.POST["password2"].strip()

        # 数据校验
        # 用户名不能为空
        if name == "":
            return render(request, "blog/reg.html", {"msg": "用户名不能为空"})
        # 判断密码是否小于6位
        if len(password) < 6:
            return render(request, "blog/reg.html", {"msg": "密码不能小于6位，请重新输入"})
        # 判断密码是否一致
        if password != password2:
            return render(request, "blog/reg.html", {"msg": "两次密码不一致"})
        # 用户名是否存在
        user = models.User.objects.filter(username=name)
        if len(user) > 0:
            return render(request, "blog/reg.html", {"msg": "用户名已存在，请重新输入"})

        # 添加用户
        try:
            user = models.User(username=name, password=password)
            user.save()
            return render(request, "blog/login.html", {"msg": "注册成功，请登录"})
        except Exception as e:
            print("添加出错，错误信息是：", e)
            return render(request, "blog/reg.html", {"msg": "注册失败，请重新注册"})


def login(request):
    if request.method == 'GET':
        return render(request, 'blog/login.html', {})
    else:
        pass

def list(request):
    user = models.User.objects.all()
    return render(request, 'blog/list.html', {"user": user})


def delete(request, id):   # 将id当成第一个参数传入，位置传参
    # 传统传参
    # id = request.GET["id"]
    print("接受到的参数是======", id)
    try:
        user = models.User.objects.get(id=id)
        user.delete()
        # return render(request, 'blog/list.html', {"msg", "删除成功"})
        return HttpResponseRedirect('/blog/list')
    except Exception as e:
        print("发现错误，错误信息是", e)
        return render(request, 'blog/list.html', {"msg", "删除失败，请重新删除"})


def update(request, id):
    user = models.User.objects.get(id=id)
    if request.method == "GET":
        return render(request, 'blog/update.html', {"user": user})
    else:
        age = request.POST["age"]
        gender = request.POST["gender"]

        user.age = age
        user.gender = gender

        try:
            user.save()
            return HttpResponseRedirect('/blog/list')
        except Exception as e:
            print("发生错误，错误信息是", e)
            return render(request, "/blog/update.html", {"user": user, "msg": "修改失败"})
