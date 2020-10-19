from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
# Create your views here.


class AuthLogin(APIView):
    authentication_classes = []
    def post(self, request):
        response = {"status": 100, "msg": None}
        username = request.data.get("username")
        password = request.data.get("password")
        print(username, password)
        user = models.User.objects.filter(username=username, password=password).first()
        if user:
            # token=get_random(name)
            # 将name进行加密,3600设定超时时间
            # token = get_token(username, 60)
            # models.UserToken.objects.update_or_create(user=user, defaults={"token": token})
            response["msg"] = "登入成功"
            # response["token"] = token
            response["name"] = user.username
        else:
            response["msg"] = "用户名或密码错误"
        return Response(response)
