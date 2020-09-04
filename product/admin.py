from django.contrib import admin
from .models import Product,Environment

# Register your models here.
# class Product_env_urlAdmim(admin.TabularInline):
#     list_display = ['id','environment','product_url']
#     model = Product
#     extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','productname','productdesc','update_time','create_time']
    # inlines = [Product_env_urlAdmin]
    admin.site.register(Product)

class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ['id','environmentname','environmentdesc','update_time','create_time']
    list_per_page = 1
admin.site.register(Environment,EnvironmentAdmin)