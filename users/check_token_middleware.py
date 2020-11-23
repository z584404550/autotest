from uuid import uuid4
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from jwt import InvalidSignatureError
from rest_framework.exceptions import ValidationError
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer


class CheckTokenMiddleware(MiddlewareMixin):
    """
    Django 1.4.x ---- Django 1.9.x
    每次请求时 判断 JWT 是否与 User.user_jwt 相等
    相等的话，说明没有以设备登录，且没有修改密码
    不相等，则说明异常设备登录，或修改了密码，修改用户的uuid并提示用户重新登录
    每次登录时记录更新JWT 为User 的一个属性user_jwt
    每次修改密码时 更新修改uuid
    """
    def procsdd_request(self, request):
        # 处理所有带JWT的请求
        jwt_token = request.MATE.get('Authorization', None)
        if jwt_token is None and jwt_token != '':
            data = {
                #     'token': jwt_token.split('')[1] # [0] 是前缀，默认为JWT
                'token': jwt_token
            }
            try:
                valid_data = VerifyJSONWebTokenSerializer().validate(data)
                user = valid_data['user']
            except (InvalidSignatureError, ValidationError):
                # 找不到用户， 说明token不合法或者身份过期
                return HttpResponse({'msg': '身份已经过期，请重新登录'}, content_type='application/json', status=400)
            else:
                # 说明进行了第二次登陆， user.user_jwt已经被重新复制，需要跟换签名。注意，此类方法将使无论是第一次登陆还是第二次登陆的人的验证消息都失效，从而保证只有一个人在线上
                if user.user_jwt != data['token']:
                    user.user_secret = uuid4()
                    user.save()
                    return HttpResponse({'msg': '异设备登录，请重新登入或修改密码'}, content_type='application/json', status=400)
        return None

    def process_response(self, request, response):
        # 处理login请求
        if response.META['PATH_INFO'] == '/users/auths/':
            # 因为登陆认证ObtainJSONWebToken继承自JSONWebTokenAPIView，所以是Response对象，不是HttpResponse对象，所以使用response.data,而不是response.content
            rep_data = response.data
            # 默认response.data里面必有token，根据序列化器VerifyJSONWebTokenSerializer()返回token和user
            valid_data = VerifyJSONWebTokenSerializer().validate(rep_data)
            user = valid_data['user']
            user.user_jwt = rep_data['token']
            user.save()
            return response

# 注销用户
# 　　user = request.user
# 　　user.user_secret = uuid4()
# 　　user.save()

# 修改密码
# 　　user.user_secret = uuid4()
# 　　user.save()
