from django.contrib import admin
from .models import Interface, ApiTest, ApiStep

# Register your models here.


class InterfaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'Product', 'Module', 'interfacename', 'interfacedesc',
                    'interfaceurl', 'request_method', 'update_time', 'create_time']
#     list_per_page = 10


class ApiStepAdmin(admin.TabularInline):
    list_display = ['id''apiname', 'apidesc', 'apiparamvalue', 'apiresult',
                    'apistep', 'apistatus', 'update_time', 'create_time']
    model = ApiStep
    extra = 1


class ApiTestAdmin(admin.ModelAdmin):
    list_display = ['id', 'apitestname', 'apitestdesc', 'apitester',
                    'apitestresult', 'create_time']
    inlines = [ApiStepAdmin]


admin.site.register(Interface, InterfaceAdmin)
admin.site.register(ApiTest, ApiTestAdmin)
admin.site.site_title = 'AutotestPlat'
admin.site.site_header = 'AtotestPlat'
