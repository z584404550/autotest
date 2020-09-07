from django.db import models
from product.models import Product,Pro_Module

# Create your models here.
# class Interface(models.Model):
#     product=models.ForeignKey('product.Product',on_delete=models.CASCADE,null=True)# 关联产品 ID，其中 product 是应用名，Product 是 product 应用的表名
#     module=models.ForeignKey('product.Promodule',on_delete=models.CASCADE,null=True)# 关联模块 ID，其中 promodule 是应用名，Promodule 是 promodule 应用的表名
#     apitestname = models.CharField('流程接口名称', max_length=64)  # 流程接口测试场景
#     apitestdesc = models.CharField('描述', max_length=64, null=True)  # 流程接口描述
#     apitester = models.CharField('测试负责人', max_length=16)  # 执行人
#     apitestresult = models.BooleanField('测试结果')  # 流程接口测试结果
#     update_time = models.DateTimeField('创建时间', auto_now=True)  # 更新时间，自动获取当前时间
#     create_time = models.DateTimeField('创建时间', auto_now_add=True)  # 创建时间，自动获取第一次时间
#     class Meta:
#         verbose_name = '流程场景接口'
#         verbose_name_plural = '流程场景接口'
#     def __str__(self):
#         return self.apitestname

class Apitest(models.Model):
    product=models.ForeignKey('product.Product',on_delete=models.CASCADE,null=True)# 关联产品 ID，其中 product 是应用名，Product 是 product 应用的表名
    # module=models.ForeignKey('product.Promodule',on_delete=models.CASCADE,null=True)# 关联模块 ID，其中 promodule 是应用名，Promodule 是 promodule 应用的表名
    apitestname = models.CharField('流程接口名称', max_length=64)  # 流程接口测试场景
    apitestdesc = models.CharField('描述', max_length=64, null=True)  # 流程接口描述
    apitester = models.CharField('测试负责人', max_length=16)  # 执行人
    apitestresult = models.BooleanField('测试结果')  # 流程接口测试结果
    update_time = models.DateTimeField('创建时间', auto_now=True)  # 更新时间，自动获取当前时间
    create_time = models.DateTimeField('创建时间', auto_now_add=True)  # 创建时间，自动获取第一次时间
    class Meta:
        verbose_name = '流程场景接口'
        verbose_name_plural = '流程场景接口'
    def __str__(self):
        return self.apitestname