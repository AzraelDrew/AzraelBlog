from Blog.models import Article, UserInfo
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password, make_password
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests
import datetime
import base64
import os
import json
hostUrl = 'http://127.0.0.1:9000/'


# 权限鉴定


@api_view(['POST'])
def azrael_checkperm(request):
    token = request.POST['token']
    content_type = request.POST['contentType']
    permissions = json.loads(request.POST['permissions'])
    # print(token)
    # print(content_type)
    # print(permissions[0])
    user_token = Token.objects.filter(key=token)
    if user_token:
        user = user_token[0].user
        for p in permissions:
            model_str = content_type.split("_")[1]
            perm_str = content_type + '.'+p+"_"+model_str
            # print(perm_str)
            check = user.has_perm(perm_str)
            print(check)
            if check == False:
                return Response("nopermission")
    else:
        return Response("nologin")

    return Response("OK")

# 登录


@api_view(['POST'])
def azrael_login(request):
    username = request.POST['username']
    password = request.POST['password']
    # 登录逻辑
    user = User.objects.filter(username=username)
    if user:
        checkPwd = check_password(password, user[0].password)
        if checkPwd:
            userinfo = UserInfo.objects.get_or_create(belong=user[0])
            userinfo = UserInfo.objects.get(belong=user[0])
            token = Token.objects.get_or_create(user=user[0])
            token = Token.objects.get(user=user[0])
        else:
            return Response('pwderr')
    else:
        return Response("none")
    userinfo_data = {
        'token': token.key,
        'nickname': userinfo.nickName,
        'headImg': userinfo.headImg,
    }
    return Response(userinfo_data)


# 自动登录
@api_view(['POST'])
def auto_login(request):
    token = request.POST['token']
    # user_token = Token.objects.get(key=token)
    user_token = Token.objects.filter(key=token)
    # print(user_token)
    # userinfo = UserInfo.objects.get(belong=user_token.user)
    # userinfo_data = {
    #     'token': token,
    #     'nickname': userinfo.nickName,
    #     'headImg': userinfo.headImg,
    # }
    # return Response(userinfo_data)

    if user_token:
        userinfo = UserInfo.objects.get(belong=user_token[0].user)
        userinfo_data = {
            'token': token,
            'nickname': userinfo.nickName,
            'headImg': userinfo.headImg,
        }
        return Response(userinfo_data)
    else:
        return Response("TokenTimeOut")


# 登出
@api_view(['POST'])
def azrael_logout(request):
    token = request.POST['token']
    user_token = Token.objects.get(key=token)
    user_token.delete()
    return Response("Logout")


# 注册
@api_view(['POST'])
def azrael_register(request):
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    # 注册逻辑
    user = User.objects.filter(username=username)
    if user:
        return Response('repeat')
    else:
        new_password = make_password(password, username)
        new_user = User(username=username, password=new_password)
        new_user.save()
    token = Token.objects.get_or_create(user=new_user)
    token = Token.objects.get(user=new_user)
    userinfo = UserInfo.objects.get_or_create(belong=new_user)
    userinfo = UserInfo.objects.get(belong=new_user)
    userinfo_data = {
        'token': token.key,
        'nickname': userinfo.nickName,
        'headImg': userinfo.headImg,
    }
    return Response(userinfo_data)

# 发布文章


@api_view(['POST'])
def add_article(request):
    title = request.POST['title']
    describe = request.POST['describe']
    cover = request.POST['cover']
    content = request.POST['content']
    token = request.POST['token']

    user_token = Token.objects.filter(key=token)

    if len(user_token) == 0:
        return Response("nologin")
    if len(title) == 0:
        return Response("notitle")
    # 保存文章
    new_article = Article(title=title)
    new_article.save()
    # 解析富文本html文档
    soup = BeautifulSoup(content, 'html.parser')
    # 获取所有的img标签 图片
    imgList = soup.find_all('img')
    # 请求远程图片
    for img in range(0, len(imgList)):
        src = imgList[img]['src']
        # 判断图片是远程还是本地
        if 'http://' in src or 'https://' in src:
            # 下载远程图片
            image = requests.get(src)
            # 转换为二进制
            image_data = Image.open(BytesIO(image.content))
            # 设置文件名称  时间 + 文章ID + 图片位标
            image_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S')+"-" + \
                str(new_article.id)+'-'+str(img)
            image_data.save('upload/'+image_name+'.png')
            new_src = hostUrl+'upload/'+image_name+'.png'
            content = content.replace(src, new_src)
            if cover == src:
                cover = new_src
        else:
            image_data = base64.b64decode(src.split(',')[1])
            image_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S')+"-"+str(new_article.id) + \
                '-'+str(img)+"."+src.split(',')[0].split('/')[1].split(';')[0]
            image_url = os.path.join('upload', image_name).replace('\\', '/')
            with open(image_url, 'wb') as f:
                f.write(image_data)
            new_src = hostUrl+image_url
            content = content.replace(src, new_src)
            if cover == src:
                cover = new_src
    new_article.content = content
    new_article.describe = describe
    new_article.cover = cover
    new_article.belong = user_token[0].user
    new_article.save()
    return Response("OK")

# 文章列表


@api_view(['GET'])
def article_list(request):
    page = request.GET['page']
    pageSize = request.GET['pageSize']

    articles = Article.objects.all()
    total = len(articles)
    paginator = Paginator(articles, pageSize)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    print(articles)
    articles_data = []
    for a in articles:
        a_item = {
            'title': a.title,
            'cover': a.cover,
            'nickName': "",
            'id': a.id
        }
        article_user = a.belong
        userinfo = UserInfo.objects.filter(belong=article_user)
        if userinfo[0].nickName:
            a_item['nickName'] = userinfo[0].nickName
        else:
            a_item['nickName'] = article_user.username
        articles_data.append(a_item)
    return Response({'data': articles_data, 'total': total})


# 删除文章

@api_view(['DELETE'])
def delete_article(request):
    article_id = request.POST['id']
    # print(article_id)
    token = request.POST['token']
    user_token = Token.objects.filter(key=token)
    if len(user_token) == 0:
        return Response("nologin")

    article = Article.objects.get(id=article_id)
    article.delete()
    return Response("OK")
