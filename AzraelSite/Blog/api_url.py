from django.urls import path
from Blog import api, blog

urlpatterns = [
    # 添加文章
    path('add-article/', api.add_article),
    # 保存图片
    path('save-img/', api.save_img),
    # 文章列表
    path('article-list/', api.article_list),
    # 删除文章
    path('delete-article/', api.delete_article),
    # 文章数据
    path('article-data/', api.article_data),

    # 用户管理
    # 登录
    path('azrael-login/', api.azrael_login),
    # 注册
    path('azrael-register/', api.azrael_register),
    path('azrael-rest-pwd/', api.azrael_reset_pwd),
    # 登出
    path('azrael-logout/', api.azrael_logout),
    # 自动登录
    path('auto-login/', api.auto_login),
    # 权限鉴定
    path('azrael-checkperm/', api.azrael_checkperm),
    # 用户列表
    path('azrael-userlist/', api.azrael_userlist),

    # 用户组
    path('azrael-group/', api.azrael_group),
    # 栏目管理
    path('azrael-lanmu/', api.azrael_lanmu),
    # 评论
    path('pinglun/', api.pinglun),
    # 收藏等信息
    path('user-article-info/', api.user_article_info),
    path('article-like/', api.articleLike),
    path('article-favor/', api.articleFavor),

    # 用户信息
    path('user-info/', api.user_info),
    path('like-info/', api.like_info),
    path('favourite-info/', api.favourite_info),

    # Blog
    path('login/', blog.Login),
    path('get/userinfo/', blog.GetUserInfo),
    path('update/userinfo/', blog.UpdateUserInfo),
    path('upload/avatar/', blog.UploadAvatar),
    path('add/article/', blog.AddArticle),
    path('article/img/', blog.ArticleImg),
    path('upadte/article/', blog.UpdateArticle),
    path('article/', blog.ArticleData),
    path('article/like/', blog.ArticleLike),
    path('article/favor/', blog.ArticleFavor),
    path('all/article/', blog.AllArtcile),
    path('my/article/', blog.MyArticle),
    path('like/article/', blog.MyLikeArticle),
    path('favourite/article/', blog.MyFavouriteArticle),
    path('comment/', blog.Comments),
    path('add/comment/', blog.AddComment),
    path('delete/comment/', blog.DeleteComment),
]
