from django.db import models
from environment.models import Environment

# Create your models here.
class Product(models.Model):
    productname=models.CharField('产品名称',max_length=64) #产品名称
    Environment = models.ForeignKey('environment.Environment', on_delete=models.CASCADE,null=True)  # 关联环境ID，其中environment是应用名，Environment是environment应用的表名
    productdesc=models.CharField('产品描述',max_length=200) #产品描述
    producturl=models.CharField('产品地址',max_length=200) #产品地址
    create_time=models.DateTimeField('创建时间',auto_now=True) #创建时间,自动获取当前时间
    class Meta:
        verbose_name='产品管理'
        verbose_name_plural='产品管理'
        def __str__(self):
            return self.productname
