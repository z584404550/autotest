from django.db import models


# Create your models here.


class Interface(models.Model):
    # 关联产品 ID，其中 product 是应用名，Product 是 product 应用的表名
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True, verbose_name='产品ID')
    # 关联模块 ID，其中 promodule 是应用名，Pro_module 是 promodule 应用的表名
    Module = models.ForeignKey('product.ProModule', on_delete=models.CASCADE, null=True, verbose_name='模块ID')
    interfacename = models.CharField(verbose_name='接口名称', max_length=64)  # 接口名称
    interfacedesc = models.CharField(verbose_name='接口描述', max_length=64, null=True)  # 接口描述
    interfaceurl = models.CharField(verbose_name='接口地址', max_length=200, null=True)  # 接口地址
    REQUEST_METHOD = (('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch'))
    request_method = models.CharField(verbose_name='请求方法', choices=REQUEST_METHOD, max_length=16, null=True)  # 请求方法
    create_time = models.DateTimeField('创建时间', auto_now_add=True)  # 创建时间，自动获取第一次时间
    update_time = models.DateTimeField('更新时间', auto_now=True)  # 更新时间，自动获取当前时间

    class Meta:
        verbose_name = '接口管理'
        verbose_name_plural = '接口管理'

    def __str__(self):
        return self.interfacename, self.interfaceurl


class ApiTest(models.Model):
    # 关联产品 ID，其中 product 是应用名，Product 是 product 应用的表名
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True, verbose_name='产品ID')
    apitestname = models.CharField(verbose_name='流程接口名称', max_length=64)  # 流程接口测试场景
    apitestdesc = models.CharField(verbose_name='描述', max_length=64, null=True)  # 流程接口描述
    apitester = models.CharField(verbose_name='测试负责人', max_length=16)  # 执行人
    apitestresult = models.BooleanField(verbose_name='测试结果')  # 流程接口测试结果
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)  # 创建时间，自动获取第一次时间
    update_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)  # 更新时间，自动获取当前时间

    class Meta:
        verbose_name = '流程场景接口'
        verbose_name_plural = '流程场景接口'

    def __str__(self):
        return self.apitestname


class ApiStep(models.Model):
    apitest = models.ForeignKey(ApiTest, on_delete=models.CASCADE, null=True, verbose_name='关联接口ID')  # 关联接口ID
    apiname = models.ForeignKey(Interface, on_delete=models.CASCADE, null=True, verbose_name='接口名称')  # 接口名称
    apidesc = models.CharField(verbose_name='接口描述', max_length=200)  # 描述
    apiparamvalue = models.CharField(verbose_name='请求参数和值', max_length=200)  # 参数和值
    apiresult = models.CharField(verbose_name='预期结果', max_length=200)  # 预期结果
    apistep = models.CharField(verbose_name='测试步聚', max_length=16, null=True)  # 测试步聚
    apistatus = models.BooleanField(verbose_name='是否通过')  # 测试结果
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)  # 创建时间，自动获取第一次时间
    update_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)  # 更新时间，自动获取当前时间

    class Meta:
        verbose_name = '流程场景接口步骤'
        verbose_name_plural = '流程场景接口步骤'

    def __str__(self):
        return self.apiname
