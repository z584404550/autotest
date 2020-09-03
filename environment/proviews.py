from django.shortcuts import render
from .models import Environment

# Create your views here.
def environment_manage(request):
    username = request.session.get('user', '')
    environment_list = Environment.objects.all()
    return render(request, "environment_manage.html", {"user": username, "environments": environment_list})