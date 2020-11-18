from django.db import models
#引用内置的user模型
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

# Create your models here.


#集成内置的user模型，并添加新的字段
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=64, verbose_name='昵称', default='')
    chocie_gender = (("male", "男"), ("female", "女"), )
    gender = models.CharField(choices=chocie_gender, default='female', max_length=6, verbose_name='性别')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=128, verbose_name='用户头像')
    user_secret = models.UUIDField(default=uuid4(), verbose_name='用户JWT秘钥')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)  # 创建时间，自动获取第一次时间
    update_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)  # 更新时间，自动获取当前时间

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'

    def __str__(self):
        return self.username
