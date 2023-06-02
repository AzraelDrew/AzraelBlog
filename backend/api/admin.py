from django.contrib import admin

from api.models import UserInfo, Article, Comment, Collect, Kudo

admin.site.register(Article)
admin.site.register(UserInfo)
admin.site.register(Comment)
admin.site.register(Kudo)
admin.site.register(Collect)
# Register your models here.
