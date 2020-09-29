from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect  # 加入引用
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import ApiTest, ApiStep
# Create your views here.


def test(request):
    return HttpResponse("Hello test")  # 返回HttpResponse响应函数


def login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password error'})

    # else:
    # context = {}
    # return render(request, 'login.html', context)
    return render(request, 'login.html')


def home(request):
    return render(request, "home.html")


# 接口管理
@login_required
def apitest_manage(request):
    apitest_list = ApiTest.objects.all()  # 读取所有流程接口数据
    username = request.session.get('user', '')  # 读取浏览器登录 Session
    return render(request, "apitest_manage.html", {"user": username, "apitests": apitest_list})  # 定义流程接口数据的变量并返回到前端


# 接口步骤管理
@login_required
def apistep_manage(request):
    username = request.session.get('user', '')
    apistep_list = ApiStep.objects.all()
    return render(request, "apistep_manage.html", {"user": username, "apisteps": apistep_list})


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')
