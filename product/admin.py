from django.contrib import admin
from .models import Product,Environment,Pro_Env_Url

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','productname','productdesc','update_time','create_time']



class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ['id','environmentname','environmentdesc','update_time','create_time']
    list_per_page = 10

# class Pro_Env_UrlAdmim(admin.TabularInline):
class Pro_Env_UrlAdmim(admin.ModelAdmin):
    list_display = ['id','Product','Environment','product_url','update_time','create_time']
    # model = Product


admin.site.register(Product,ProductAdmin)
admin.site.register(Environment,EnvironmentAdmin)
admin.site.register(Pro_Env_Url,Pro_Env_UrlAdmim)