from django.db import models

# Create your models here.
class Product(models.Model):
    productname = models.CharField('产品名称',max_length=64) #产品名称
    productdesc = models.CharField('产品描述',max_length=200) #产品描述
    update_time = models.DateTimeField('修改时间',auto_now=True) #修改时间,自动获取当前时间
    create_time = models.DateTimeField('创建时间', auto_now_add=True)  # 创建时间,自动获取第一次创建时间
    class Meta:
        verbose_name='产品管理'
        verbose_name_plural='产品管理'
    def __str__(self):
        return self.productname

class Environment(models.Model):
    environmentname=models.CharField('环境名称',max_length=64) #环境名称
    environmentdesc=models.CharField('环境描述',max_length=200) #环境描述
    update_time = models.DateTimeField('修改时间',auto_now=True) #修改时间,自动获取当前时间
    create_time = models.DateTimeField('创建时间', auto_now_add=True)  # 创建时间,自动获取第一次创建时间
    class Meta:
        verbose_name='环境管理'
        verbose_name_plural='环境管理'
    def __str__(self):
        return self.environmentname

class Pro_Env_Url(models.Model):
    Product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    Environment = models.ForeignKey('Environment', on_delete=models.CASCADE,null=True)  # 关联环境ID，其中environment是应用名，Environment是environment应用的表名
    product_url = models.CharField('产品地址',max_length=200) #产品地址
    update_time = models.DateTimeField('修改时间',auto_now=True) #修改时间,自动获取当前时间
    create_time = models.DateTimeField('创建时间', auto_now_add=True)  # 创建时间,自动获取第一次创建时间
    def __str__(self):
        return self.product_url
    class Meta:
        verbose_name='产品地址'
        verbose_name_plural='产品地址'

class Pro_Module(models.Model):
    Product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    modulename = models.CharField('模块名称', max_length=16)  # 模块名称
    moduleurl = models.CharField('地址地址',max_length=32) #模块地址
    update_time = models.DateTimeField('修改时间',auto_now=True) #修改时间,自动获取当前时间
    create_time = models.DateTimeField('创建时间', auto_now_add=True)  # 创建时间,自动获取第一次创建时间
    def __str__(self):
        return self.modulename
    class Meta:
        verbose_name='模块管理'
        verbose_name_plural='模块管理'