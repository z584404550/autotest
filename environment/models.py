from django.db import models

# Create your models here.
class Environment(models.Model):
    environmentname=models.CharField('环境名称',max_length=64) #环境名称
    environmentdesc=models.CharField('环境描述',max_length=200) #环境描述
    create_time=models.DateTimeField('创建时间',auto_now=True) #创建时间
    class Meta:
        verbose_name='环境管理'
        verbose_name_plural='环境管理'
        def __str__(self):
            return self.environmentname