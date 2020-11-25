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
from apitest import apitestviews
from product import proviews
from set import setviews
from bug import bugviews
from users import utils, usersviews
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', utils.obtain_jwt_token),
    # path('login/', views.login),
    path('home/', apitestviews.home),
    path('logout/', apitestviews.logout, name='login'),
    path('environment_manage/', proviews.environment_manage),
    path('product_manage/', proviews.product_manage),
    path('proenvurl_manage/', proviews.proenvurl_manage),
    path('promodule_manage/', proviews.promodule_manage),
    path('apitest_manage/', apitestviews.apitest_manage),
    path('apistep_manage/', apitestviews.apistep_manage, name='apistep_manage'),
    path('bug_manage/', bugviews.bug_manage),
    path('test_report/', apitestviews.test_report),
    path('set_user', setviews.set_user),
    path('left/', apitestviews.left),
    path('apisearch/', apitestviews.apisearch),
    path('welcome/', apitestviews.welcome),
    path('periodic_task/', apitestviews.periodic_task),
    path('tasksearch/', apitestviews.tasksearch),
    path(r'', TemplateView.as_view(template_name='index.html')),
    # 获取
    path('api-token-auth/', utils.obtain_jwt_token),
    # 刷新
    path('api-token-refresh/', utils.refresh_jwt_token),
    # 校验
    path('api-token-verify/', utils.verify_jwt_token),
    path('user/', usersviews.UserProfile.as_view())
]
