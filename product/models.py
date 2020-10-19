from django.db import models

# Create your models here.


class Product(models.Model):
    productname = models.CharField(verbose_name='产品名称', max_length=64)  # 产品名称
    productdesc = models.CharField(verbose_name='产品描述', max_length=200)  # 产品描述
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)  # 创建时间，自动获取第一次时间
    update_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)  # 更新时间，自动获取当前时间

    class Meta:
        verbose_name = '产品管理'
        verbose_name_plural = '产品管理'

    def __str__(self):
        return self.productname


class Environment(models.Model):
    environmentname = models.CharField(verbose_name='环境名称', max_length=64)  # 环境名称
    environmentdesc = models.CharField(verbose_name='环境描述', max_length=200)  # 环境描述
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)  # 创建时间，自动获取第一次时间
    update_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)  # 更新时间，自动获取当前时间

    class Meta:
        verbose_name = '环境管理'
        verbose_name_plural = '环境管理'

    def __str__(self):
        return self.environmentname


class ProEnvUrl(models.Model):
    Product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, verbose_name='环境ID')
    # 关联环境ID，其中environment是应用名，Environment是environment应用的表名
    Environment = models.ForeignKey('Environment', on_delete=models.CASCADE, null=True, verbose_name='模块ID')
    producturl = models.CharField(verbose_name='产品地址', max_length=200)  # 产品地址
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)  # 创建时间，自动获取第一次时间
    update_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)  # 更新时间，自动获取当前时间

    def __str__(self):
        return self.producturl

    class Meta:
        verbose_name = '产品地址'
        verbose_name_plural = '产品地址'


class ProModule(models.Model):
    Product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, verbose_name='产品ID')
    modulename = models.CharField(verbose_name='模块名称', max_length=16)  # 模块名称
    moduleurl = models.CharField(verbose_name='地址地址', max_length=32)  # 模块地址
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)  # 创建时间，自动获取第一次时间
    update_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)  # 更新时间，自动获取当前时间

    def __str__(self):
        return self.modulename

    class Meta:
        verbose_name = '模块管理'
        verbose_name_plural = '模块管理'
