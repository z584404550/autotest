from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile
from .api.UserProfile import UserSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# Create your views here.
class UserList(APIView):
    authentication_classes = [JSONWebTokenAuthentication,]

    def get(self, request):
        queryset = UserProfile.objects.all()
        serializer = UserSerializer(instance=queryset, many=True)
        return Response(serializer.data)
