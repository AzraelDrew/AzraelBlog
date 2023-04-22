from django.contrib import admin
from Blog.models import Article, UserInfo, Lanmu, Pinglun, Like, Favourite
# Register your models here.

admin.site.register(Article)
admin.site.register(UserInfo)
admin.site.register(Lanmu)
admin.site.register(Pinglun)
admin.site.register(Like)
admin.site.register(Favourite)


admin.site.site_header = 'RainBlog管理后台'  # 设置header
admin.site.site_title = 'RainBlogg管理后台管理后台'   # 设置title
admin.site.index_title = 'RainBlog管理后台管理后台'