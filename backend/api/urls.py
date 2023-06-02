from django.urls import path

from api.views import article, collect, comment, kudo, user
urlpatterns = [
    path('token/', user.TokenView.as_view()),
    path('login/', user.LoginView.as_view({'post': 'login'})),
    path('user/',
         user.UserView.as_view({"get": "list", "post": "create"})),
    path('user/<int:pk>', user.UserView.as_view(
        {"get": "retrieve", "put": "update", "delete": "destroy"})),
    path('article/',
         article.ArticleView.as_view({"get": "list", "post": "create"})),
    path('article/<int:pk>', article.ArticleView.as_view(
        {"get": "retrieve", "put": "update", "delete": "destroy"})),
    path('comment/',
         comment.ComentView.as_view({"get": "list", "post": "create"})),
    path('comment/<int:pk>', article.ArticleView.as_view(
        {"get": "retrieve", "put": "update", "delete": "destroy"})),
    path('collect/',
         collect.CollectView.as_view({"get": "list", "post": "collect"})),
    path('collect/<int:pk>',
         article.ArticleView.as_view({"delete": "destroy"})),
    path('kudo/',
         kudo.KudoView.as_view({"get": "list", "post": "kudo"})),
    path('kudo/<int:pk>',
         kudo.KudoView.as_view({"delete": "destroy"})),
]
