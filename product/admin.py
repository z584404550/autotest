from django.contrib import admin
from .models import Product, Environment, ProEnvUrl, ProModule

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'productname', 'productdesc', 'update_time', 'create_time']
    list_per_page = 10


class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'environmentname', 'environmentdesc', 'update_time', 'create_time']
    list_per_page = 10


class ProEnvUrlAdmim(admin.ModelAdmin):
    list_display = ['id', 'Product', 'Environment', 'producturl', 'update_time', 'create_time']
    list_per_page = 10


class ProModuleAdmin(admin.ModelAdmin):
    list_display = ['id', 'Product', 'modulename', 'moduleurl', 'update_time', 'create_time']
    list_per_page = 10


admin.site.register(Product, ProductAdmin)
admin.site.register(Environment, EnvironmentAdmin)
admin.site.register(ProEnvUrl, ProEnvUrlAdmim)
admin.site.register(ProModule, ProModuleAdmin)
