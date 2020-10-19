from django.db import models
from product.models import Product

# Create your models here.


class Bug(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True, verbose_name='产品ID')  # 关联产品ID
    bugname = models.CharField('bug 名称', max_length=64, verbose_name='Bug名称')  # Bug 名称
    bugdetail = models.CharField('详情', max_length=200, verbose_name='详情')  # 详情
    BUG_STATUS = (('激活', '激活'), ('已解决', '已解决'), ('已关闭', '已关闭'))
    bugstatus = models.CharField(verbose_name='解决状态', choices=BUG_STATUS, default='激活', max_length=200,
                                 null=True)  # 解决状态
    BUG_LEVEL = (('1', '1'), ('2', '2'), ('3', '3'))
    buglevel = models.CharField(verbose_name='严重程度', choices=BUG_LEVEL, default='3', max_length=200, null=True)  # 严重程度
    bugcreater = models.CharField('创建人', max_length=200, verbose_name='创建人')  # 创建人
    bugassign = models.CharField('分配给', max_length=200, verbose_name='被分配人')  # 分配给
    create_time = models.DateTimeField('创建时间', auto_now_add=True, verbose_name='创建时间')  # 创建时间，自动获取第一次时间
    update_time = models.DateTimeField('创建时间', auto_now=True, verbose_name='更新时间')  # 更新时间，自动获取当前时间

    class Meta:
        verbose_name = 'bug 管理'
        verbose_name_plural = 'bug 管理'

    def __str__(self):
        return self.bugname
