from django.contrib import admin
from .models import Environment

# Register your models here.
class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ['id','environmentname','environmentdesc','create_time']
    admin.site.register(Environment) # 把环境模块注册到 Django admin 后台并能显示