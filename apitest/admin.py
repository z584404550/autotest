from django.contrib import admin
from .models import Interface, Apitest, Apistep

# Register your models here.


class InterfaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'Product', 'Module', 'interfecename', 'interfacedesc',
                    'interfaceurl', 'request_method', 'update_time', 'create_time']
#     list_per_page = 10


class ApistepAdmin(admin.TabularInline):
    list_display = ['id''apiname', 'apidesc', 'apiparamvalue', 'apiresult',
                    'apistep', 'apistatus', 'update_time', 'create_time']
    model = Apistep
    extra = 1


class ApitestAdmin(admin.ModelAdmin):
    list_display = ['id', 'apitestname', 'apitestdesc', 'apitester',
                    'apitestresult', 'create_time']
    inlines = [ApistepAdmin]


admin.site.register(Interface, InterfaceAdmin)
admin.site.register(Apitest, ApitestAdmin)
