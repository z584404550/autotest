from django.shortcuts import render
from .models import Environment, Product, ProModule, ProEnvUrl

# Create your views here.


def environment_manage(request):
    username = request.session.get('user', '')
    environment_list = Environment.objects.all()
    return render(request, "environment_manage.html", {"user": username, "environments": environment_list})


def product_manage(request):
    username = request.session.get('user', '')
    product_list = Product.objects.all()
    return render(request, "product_manage.html", {"user": username, "products": product_list})


def proenvurl_manage(request):
    username = request.session.get('user', '')
    proenvurl_list = ProEnvUrl.objects.all()
    return render(request, "proenvurl_manage.html", {"user": username, "proenvurls": proenvurl_list})


def promodule_manage(request):
    username = request.session.get('user', '')
    promodule_list = ProModule.objects.all()
    return render(request, "promodule_manage.html", {"user": username, "promodules": promodule_list})
