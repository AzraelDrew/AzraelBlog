

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# from datetime import datetime
# Create your models here.

# 用户信息


class UserInfo(models.Model):
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=32)
    nickname = models.CharField(blank=True, max_length=32)
    user = models.OneToOneField(
        User, blank=True, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, upload_to="avatar")
    description = models.CharField(blank=True, max_length=512)
    phone = models.CharField(blank=True, max_length=11)

    class Meta:
        verbose_name = "用户"

    def __str__(self):
        return self.username

# 文章


class Article(models.Model):
    title = models.CharField(max_length=80)
    cover = models.ImageField(blank=True, upload_to="cover")
    description = models.CharField(blank=True, max_length=200)
    content = models.TextField()
    relate_user = models.ForeignKey(
        UserInfo, on_delete=models.CASCADE, related_name='user_article')
    view = models.IntegerField(default=0)

    date = models.DateTimeField(default=now)

    class Meta:
        verbose_name = "文章"


# 评论
class Comment(models.Model):
    relate_user = models.ForeignKey(UserInfo,
                                    on_delete=models.CASCADE,
                                    related_name='comment_user')
    relate_article = models.ForeignKey(Article,
                                       on_delete=models.CASCADE,
                                       related_name='comment_article')
    text = models.TextField(max_length=512)
    date = models.DateTimeField(default=now)

    class Meta:
        verbose_name = "评论"


# 收藏
class Collect(models.Model):
    relate_user = models.ForeignKey(UserInfo,
                                    on_delete=models.CASCADE,
                                    related_name='collect_user')
    relate_article = models.ForeignKey(Article,
                                       on_delete=models.CASCADE,
                                       related_name='collect_article')
    status = models.BooleanField(default=1)

    class Meta:
        verbose_name = "收藏"

    def __str__(self):
        return self.relate_user.username + "对" + self.relate_article.title + "收藏"


# 点赞


class Kudo(models.Model):
    relate_user = models.ForeignKey(UserInfo,
                                    on_delete=models.CASCADE,
                                    related_name='kudo_user')
    relate_article = models.ForeignKey(Article,
                                       on_delete=models.CASCADE,
                                       related_name='kudo_article')
    status = models.BooleanField(default=1)

    class Meta:
        verbose_name = "点赞"

    def __str__(self):
        return self.relate_user.username + "对" + self.relate_article.title + "点赞"
