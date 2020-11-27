from rest_framework import generics, serializers
from ..models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=False, allow_null=False, max_length=150)
    password = serializers.CharField(required=False, allow_null=False, max_length=128)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'password']
