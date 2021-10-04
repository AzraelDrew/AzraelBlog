from django.contrib import admin
from Blog.models import Article, UserInfo, Lanmu, Pinglun, Like, Favourite
# Register your models here.

admin.site.register(Article)
admin.site.register(UserInfo)
admin.site.register(Lanmu)
admin.site.register(Pinglun)
admin.site.register(Like)
admin.site.register(Favourite)
