from django.urls import path
from Blog import api

urlpatterns = [
    # 添加文章
    path('add-article/', api.add_article),
    # 文章列表
    path('atricle-list/', api.article_list),
    # 删除文章

    path('delete-article/', api.delete_article),
    # 用户管理
    # 登录
    path('azrael-login/', api.azrael_login),
    # 注册
    path('azrael-register/', api.azrael_register),
    # 登出
    path('azrael-logout/', api.azrael_logout),
    # 自动登录
    path('auto-login/', api.auto_login),
    # 权限鉴定
    path('azrael-checkperm/', api.azrael_checkperm),



]
