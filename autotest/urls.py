"""autotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apitest import views
from product import proviews
from set import setviews
from bug import bugviews
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('home/', views.home),
    path('logout/', views.logout),
    path('environment_manage/', proviews.environment_manage),
    path('product_manage/', proviews.product_manage),
    path('proenvurl_manage/', proviews.proenvurl_manage),
    path('promodule_manage/', proviews.promodule_manage),
    path('apitest_manage/', views.apitest_manage),
    path('apistep_manage/', views.apistep_manage, name='apistep_manage'),
    path('bug_manage/', bugviews.bug_manage),
    path('test_report/', views.test_report),
    path('set_user', setviews.set_user),
    path('left/', views.left),
    path('apisearch/', views.apisearch),
    path('welcome/', views.welcome),
    path('periodic_task/', views.periodic_task),
    path('tasksearch/', views.tasksearch),
    path(r'', TemplateView.as_view(template_name='index.html')),
]
