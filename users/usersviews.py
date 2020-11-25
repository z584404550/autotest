from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile
from .api.UserProfile import UserSerializer

# Create your views here.
class UserProfile(APIView):
    def get(self, request, id):
        queryset = UserProfile.objects.get(id=id)
        serializer = UserSerializer(instance=queryset, many=True)
        return Response(serializer.data)
