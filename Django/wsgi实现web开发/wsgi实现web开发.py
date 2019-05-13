from wsgiref.simple_server import make_server


def log(response):
    msg = "欢迎进入我们的登录页面"
    msg += "<br><a href ='/list'>返回详情</a>"
    return [msg.encode("utf-8")]


def reg(response):
    msg = "欢迎进入我们的注册页面"
    msg += "<br><a href ='/log'>返回登录</a>"
    return [msg.encode("utf-8")]


def list(response):
    msg = "欢迎进入我们的详情页面"
    msg += "<br><a href ='/'>返回首页</a>"
    return [msg.encode("utf-8")]


def index(env, response):
    response("200 OK", [("Content-Type", "text/html;charset=utf-8")])
    # print(env["QUERY_STRING"])
    path_info = env["PATH_INFO"][1:]
    print(path_info)
    # print(env["PATH_INFO"])
    # return [b'hello world']
    if path_info == "log":
        return log(response)
    elif path_info == "reg":
        return reg(response)
    elif path_info == "list":
        return list(response)
    else:
        msg = "欢迎访问我们的首页面"
        msg += "<br><a href ='/log'>返回登录页面</a>"
        msg += "<br><a href ='/reg'>返回注册页面</a>"
        msg += "<br><a href ='/list'>返回详情页面</a>"
        return [msg.encode("utf-8")]


server = make_server("", 8080, app=index)
print("server running......")
server.serve_forever()