from rest_framework import generics, serializers
from ..models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=False, allow_null=False, max_length=150)
    password = serializers.CharField(required=False, allow_null=False, max_length=128)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'password']

class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False, validators=[UniqueValidator(queryset=UserProfile.objects.all(), message='用户已存在')])
