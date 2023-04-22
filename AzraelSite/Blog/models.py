from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

from datetime import datetime
from django.utils.timezone import now
# Create your models here.

# 用户信息


class UserInfo(models.Model):
    nickName = models.CharField(null=True, blank=True, max_length=200)
    headImg = models.CharField(
        max_length=200, default='http://127.0.0.1:8000/upload/default.png')
    desc = models.CharField(null=True, blank=True, max_length=512)
    phone = models.CharField(null=True, blank=True, max_length=11)
    belong = models.OneToOneField(User,
                                  on_delete=models.CASCADE,
                                  null=True,
                                  blank=True)
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __int__(self):
        return self.id


# 文章分类
class Lanmu(models.Model):
    name = models.CharField(null=True, blank=True, max_length=80)
    belong = models.ForeignKey("self",
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True,
                               related_name='lanmu_children')
    class Meta:
        verbose_name = "栏目"
        verbose_name_plural = "栏目"
    def __str__(self):
        return self.name


# 文章


class Article(models.Model):
    title = models.CharField(null=True, blank=True, max_length=80)
    cover = models.CharField(
        null=True,
        blank=True,
        max_length=300,
    )
    describe = models.CharField(null=True, blank=True, max_length=200)
    content = models.TextField()
    belong = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               related_name='article_user')
    belong_lanmu = models.ForeignKey(Lanmu,
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     blank=True,
                                     related_name='article_lanmu')

    view = models.IntegerField(default=0)

    date = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )
    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"
    def __int__(self):
        return self.id


# 评论


class Pinglun(models.Model):
    belong_user = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    null=True,
                                    blank=True,
                                    related_name='pinglun_user')
    belong = models.ForeignKey(Article,
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               related_name='pinglun_article')
    text = models.CharField(null=True, blank=True, max_length=120)

    # date = models.DateTimeField(
    #     auto_now_add=True,
    #     null=True,
    #     blank=True,
    # )

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"
    date = models.DateTimeField(default=now)

    def __int__(self):
        return self.id


# 收藏
class Favourite(models.Model):
    belong_user = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    null=True,
                                    blank=True,
                                    related_name='favor_user')
    belong = models.ForeignKey(Article,
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               related_name='favor_article')
    class Meta:
        verbose_name = "收藏"
        verbose_name_plural = "收藏"
    def __str__(self):
        return self.belong_user.username + self.belong.title


# 点赞


class Like(models.Model):
    belong_user = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    null=True,
                                    blank=True,
                                    related_name='like_user')
    belong = models.ForeignKey(Article,
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               related_name='like_article')
    class Meta:
        verbose_name = "点赞"
        verbose_name_plural = "点赞"
    def __str__(self):
        return self.belong_user.username + self.belong.title


# 打赏

# class PayOrder(models.Model):
#     order = models.CharField(null=True, blank=True, max_length=80)
#     price = models.CharField(null=True, blank=True, max_length=80)
#     status = models.BooleanField(default=False, null=True, blank=True)
#     belong_user = models.ForeignKey(
#         User, on_delete=models.CASCADE, null=True, blank=True, related_name='order_user')
#     belong = models.ForeignKey(Article, on_delete=models.CASCADE,
#                                null=True, blank=True, related_name='order_article')

#     def __int__(self):
#         return self.id
