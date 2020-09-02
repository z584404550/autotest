from django.shortcuts import render
from django.http import HttpResponse #加入引用
# Create your views here.
def test(request):
    return HttpResponse("Hello test") #返回HttpResponse响应函数
def login(request):
    return render(request,'login.html')