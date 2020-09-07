from django.db import models
from product.models import Product,Pro_Module

# Create your models here.
class Interface(models.Model):
    Product=models.ForeignKey('product.Product',on_delete=models.CASCADE,null=True)# 关联产品 ID，其中 product 是应用名，Product 是 product 应用的表名
    Module=models.ForeignKey('product.Pro_Module',on_delete=models.CASCADE,null=True)# 关联模块 ID，其中 promodule 是应用名，Pro_module 是 promodule 应用的表名
    interfecename=models.CharField('接口名称',max_length=64) #接口名称
    interfacedesc = models.CharField('接口描述', max_length=64, null=True)  # 接口描述
    interfaceurl = models.CharField('接口地址', max_length=200, null=True)  # 接口地址
    REQUEST_METHOD = (('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch'))
    request_method = models.CharField(verbose_name='请求方法', choices=REQUEST_METHOD,max_length=16,null=True)  # 请求方法
    update_time = models.DateTimeField('创建时间', auto_now=True)  # 更新时间，自动获取当前时间
    create_time = models.DateTimeField('创建时间', auto_now_add=True)  # 创建时间，自动获取第一次时间
    class Meta:
        verbose_name = '接口管理'
        verbose_name_plural = '接口管理'
    def __str__(self):
        return self.interfecename

class Apitest(models.Model):
    product=models.ForeignKey('product.Product',on_delete=models.CASCADE,null=True)# 关联产品 ID，其中 product 是应用名，Product 是 product 应用的表名
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

class Apistep(models.Model):
    apitest=models.ForeignKey(Apitest,on_delete=models.CASCADE,null=True) #关联接口ID
    apiname = models.ForeignKey(Interface,on_delete=models.CASCADE,null=True)  # 接口名称
    apidesc = models.CharField('接口描述',max_length=200)  # 描述
    apiparamvalue = models.CharField('请求参数和值',max_length=200) # 参数和值
    apiresult = models.CharField('预期结果',max_length=200) # 预期结果
    apistep = models.CharField('测试步聚',max_length=16,null=True) # 测试步聚
    apistatus = models.BooleanField('是否通过') # 测试结果
    update_time = models.DateTimeField('创建时间', auto_now=True)  # 更新时间，自动获取当前时间
    create_time = models.DateTimeField('创建时间',auto_now_add=True) # 创建时间，自动获取第一次时间
    def __str__(self):
        return self.apiname
