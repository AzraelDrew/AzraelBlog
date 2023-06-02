from Blog.models import Article, UserInfo, Pinglun, Like, Favourite
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password, make_password
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
import datetime
import os

hostUrl = 'http://127.0.0.1:8000/'

# hostUrl = 'http://43.138.126.114:8000/'


def CurrentUserId(token):
    exists = Token.objects.filter(key=token).exists()
    if exists:
        id = Token.objects.filter(key=token).first().user_id
    else:
        id = 0
    return id


def ResUserInfo(token):
    userId = CurrentUserId(token)
    print(userId)
    username = User.objects.get(id=userId).username
    userinfo = UserInfo.objects.get(belong_id=userId)
    userinfoData = {
        "userId": userId,
        'token': token,
        'name': username,
        'nickname': userinfo.nickName,
        'avatar': userinfo.headImg,
        'phone': userinfo.phone,
        'desc': userinfo.desc,
    }
    return userinfoData


def GetArticle(userId, article):
    data = {
        'title':
        article.title,
        'cover':
        article.cover,
        'nickName':
        '',
        'id':
        article.id,
        'content':
        article.content,
        'date':
        article.date,
        "viewNumber":
        article.view,
        'likeNumber':
        Like.objects.filter(belong_id=article.id).count(),
        'favouriteNumber':
        Favourite.objects.filter(belong_id=article.id).count(),
        'commentNumber':
        Pinglun.objects.filter(belong_id=article.id).count(),
        'userAvatar':
        UserInfo.objects.get(belong_id=article.belong_id).headImg,
        'belonguser':
        UserInfo.objects.get(belong_id=article.belong_id).nickName,
        'likeStatus':
        Like.objects.filter(belong_id=article.id,
                            belong_user_id=userId).exists(),
        'favorStatus':
        Favourite.objects.filter(belong_id=article.id,
                                 belong_user_id=userId).exists(),
    }
    article_user = article.belong
    userinfo = UserInfo.objects.get(belong=article_user)
    if userinfo.nickName:
        data['nickName'] = userinfo.nickName
    else:
        data['nickName'] = article_user.username
    return data


@api_view(['POST'])
def Login(request):
    username = request.data['username']
    password = request.data['password']
    # 登录逻辑
    user = User.objects.filter(username=username).first()

    if user:
        nickName = UserInfo.objects.get(belong_id=user.id).nickName
        desc = UserInfo.objects.get(belong_id=user.id).desc
        phone = UserInfo.objects.get(belong_id=user.id).phone
        checkPwd = check_password(password, user.password)
        if checkPwd:
            userinfo = UserInfo.objects.get_or_create(belong=user)
            userinfo = UserInfo.objects.get(belong=user)
            token = Token.objects.get_or_create(user=user)
            token = Token.objects.get(user=user)
        else:
            return Response('pwderr')
    else:
        return Response("none")
    userinfo_data = {
        "userId": userinfo.id,
        'token': token.key,
        'name': str(user),
        'nickname': nickName,
        'avatar': userinfo.headImg,
        'phone': phone,
        'desc': desc,
    }
    return Response(userinfo_data)

# 注册


@api_view(['POST'])
def Register(request):
    username = request.data['username']
    password = request.data['password']
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
    userinfo = UserInfo.objects.get_or_create(belong=new_user,
                                              nickName=username)
    userinfo = UserInfo.objects.get(belong=new_user)
    userinfo_data = {
        'token': token.key,
        'nickname': str(username),
        'headImg': userinfo.headImg,
    }
    return Response(userinfo_data)


# 重置密码
@api_view(['POST'])
def ResetPassword(request):
    username = request.data['username']
    password = request.data['password']
    # 注册逻辑
    user = User.objects.filter(username=username)
    if not user:
        return Response('not_exist')
    else:
        new_password = make_password(password, username)
        User.objects.filter(username=username).update(password=new_password)
        return Response("OK")


@api_view(["POST"])
def GetUserInfo(request):
    if not request.data['token']:
        userinfo = {
            "userId": 0,
            'token': 'token',
            'name': '',
            'nickname': '未登录',
            'avatar': hostUrl + 'upload/' + "default.png",
            'phone': '',
            'desc': '',
        }
    else:
        userinfo = ResUserInfo(request.data['token'])
    return Response(userinfo)


@api_view(["POST"])
def UpdateUserInfo(request):
    token = request.data["token"]
    id = CurrentUserId(token)
    name = request.data["name"]
    nickName = request.data["nickName"]
    avatar = request.data["avatar"]
    phone = request.data["phone"]
    desc = request.data["desc"]
    User.objects.filter(id=id).update(username=name)
    UserInfo.objects.filter(belong_id=id).update(headImg=avatar,
                                                 nickName=nickName,
                                                 desc=desc,
                                                 phone=phone)
    return Response("ok")


@api_view(('GET', "POST"))
def UploadAvatar(request):
    if request.method == "POST":
        print("UploadImg")
        avatar = request.FILES["avatar"]
        image_name = datetime.datetime.now().strftime(
            '%Y%m%d%H%M%S') + "." + str(avatar).split(".")[1]
        print(image_name)
        image_name = os.path.join('upload', image_name).replace('\\', '/')
        print(image_name)
        f = open(image_name, mode="wb")
        for chunk in avatar.chunks():
            f.write(chunk)
        f.close()
        url = hostUrl + image_name
        # print(url)
        data = {"url": url}
        return Response(data)


def UserLoginAndPerm(token, permList):
    user_token = Token.objects.filter(key=token)
    print('UserLoginAndPerm', user_token)
    if user_token:
        user = user_token[0].user
        for perm_str in permList:
            perm_user = user.has_perm(perm_str)
            if perm_user:
                return 'perm_pass'
            else:
                return 'noperm'
    else:
        return 'nologin'


@api_view(['POST', 'PUT'])
def AddArticle(request):
    title = request.data['title']
    describe = request.data['describe']
    content = request.data['content']
    token = request.data["token"]
    id = CurrentUserId(token)
    cover = hostUrl + 'upload/' + 'defaultCover.png'
    user_token = Token.objects.filter(user_id=id).first()
    # 保存文章
    article = Article.objects.create(title=title,
                                     cover=cover,
                                     content=content,
                                     describe=describe,
                                     belong=user_token.user)
    print(article)
    return Response({"status": "OK", "id": article.id, "text": "文章发布成功"})


@api_view(['POST'])
def DeleteArticle(request):
    Article.objects.filter(id=request.data['id']).delete()
    return Response({"status": "ok", "text": "删除文章成功"})
# markdown上传本地图片


@api_view(['POST', 'PUT'])
def ArticleImg(request):
    src = request.data['imgnode']
    src.name = datetime.datetime.now().strftime(
        '%Y%m%d%H%M%S') + "." + src.name.split(".")[1]
    image_url = os.path.join('upload', src.name).replace('\\', '/')
    f = open(image_url, mode="wb")
    for chunk in src.chunks():
        f.write(chunk)
    f.close()
    image_url = {'url': hostUrl + image_url}
    return Response(image_url)


@api_view(["POST"])
def UpdateArticle(request):
    articleId = request.data["articleId"]
    title = request.data['title']
    describe = request.data['describe']
    content = request.data['content']
    token = request.data["token"]
    id = CurrentUserId(token)
    cover = hostUrl + 'upload/' + 'defaultCover.png'

    user_token = Token.objects.filter(user_id=id).first()
    # 更新文章
    Article.objects.filter(id=articleId).update(title=title,
                                                content=content,
                                                describe=describe,
                                                belong=user_token.user)
    return Response("OK")


@api_view(["GET"])
def AllArtcile(request):
    search_value = request.GET.get("search", "")
    data_dict = {}
    if search_value:
        print(search_value)

        data_dict["title__contains"] = search_value
        articles = Article.objects.filter(**data_dict).order_by('-id')
    page = request.GET["page"]
    pageSize = request.GET["pageSize"]
    userId = request.GET['userId']
    if not userId:
        userId = 0
    # articles = Article.objects.all().order_by('id')
    articles = Article.objects.filter(**data_dict).order_by('-id')
    total = len(articles)
    paginator = Paginator(articles, pageSize)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    articles_data = []
    for item in articles:
        data = GetArticle(userId, item)
        articles_data.append(data)
    return Response({'data': articles_data, 'total': total})


@api_view(['GET'])
def ArticleData(request):
    article_id = request.GET['id']
    userId = request.GET['userId']
    if not userId:
        userId = 0
    article = Article.objects.get(id=article_id)
    userinfo = UserInfo.objects.get(belong_id=article.belong_id)
    Article.objects.filter(id=article_id).update(view=article.view + 1)
    article_data = {
        'id':
        article_id,
        "title":
        article.title,
        "ddescribe":
        article.describe,
        'date':
        article.date,
        "content":
        article.content,
        "nickName":
        userinfo.nickName,
        "avatar":
        userinfo.headImg,
        "commentNumber":
        Pinglun.objects.filter(belong_id=article_id).count(),
        "favouriteNumber":
        Favourite.objects.filter(belong_id=article_id).count(),
        "likeNumber":
        Like.objects.filter(belong_id=article_id).count(),
        "viewNumber":
        article.view,
        'likeStatus':
        Like.objects.filter(belong_id=article_id,
                            belong_user_id=userId).exists(),
        'favorStatus':
        Favourite.objects.filter(belong_id=article_id,
                                 belong_user_id=userId).exists(),
        'belongUser':
        article.belong_id
    }

    return Response(article_data)


@api_view(['GET'])
def Comments(request):
    article_id = request.GET['id']
    # pagesize = 10
    pagesize = Pinglun.objects.all().count()
    page = 1
    article = Article.objects.get(id=article_id)

    pingluns = Pinglun.objects.filter(belong=article).order_by('-id')

    total = len(pingluns)
    paginator = Paginator(pingluns, pagesize)
    try:
        pingluns = paginator.page(page)
    except PageNotAnInteger:
        pingluns = paginator.page(1)
    except EmptyPage:
        pingluns = paginator.page(paginator.num_pages)

    pinglun_data = []
    for pinglun in pingluns:
        pinglun_item = {
            'id':
            pinglun.id,
            "nickName":
            UserInfo.objects.filter(
                belong_id=pinglun.belong_user_id).first().nickName,
            "text":
            pinglun.text,
            'date':
            pinglun.date,
            "avatar":
            UserInfo.objects.filter(
                belong_id=pinglun.belong_user_id).first().headImg
        }
        pinglun_data.append(pinglun_item)
    return Response({"data": pinglun_data, "total": total})


@api_view(["POST"])
def AddComment(request):
    articleId = request.data["id"]
    currentId = request.data["userId"]
    comment = request.data["text"]

    new_pinglun = Pinglun(belong_user_id=currentId,
                          belong_id=articleId,
                          text=comment)
    new_pinglun.save()
    comment_num = Pinglun.objects.filter(belong_id=articleId).count()
    return Response({"status": "OK", "text": "发布评论成功", "commentNumber": comment_num})


@api_view(["POST"])
def DeleteComment(request):
    pinlunId = request.data["id"]
    currentId = request.data["userId"]
    print(pinlunId, currentId)
    currentPinLun = Pinglun.objects.filter(id=pinlunId,
                                           belong_user_id=currentId).first()

    if currentPinLun:
        currentPinLun.delete()
    else:
        return Response("none")
    return Response("OK")


@api_view(['GET', 'POST'])
def ArticleLike(request):
    if request.method == "POST":
        articleId = request.data['id']
        userId = request.data['userId']
    if request.method == "GET":
        articleId = request.GET['id']
        userId = request.GET['userId']

    article = Article.objects.get(id=articleId)

    liked = Like.objects.filter(belong=article, belong_user_id=userId)

    if liked:
        liked[0].delete()
        return Response({"status": False, "text": "取消点赞"})
    else:
        new_like = Like(belong=article, belong_user_id=userId)
        new_like.save()
        return Response({"status": True, "text": "点赞成功"})


@api_view(['GET', 'POST'])
def ArticleFavor(request):
    if request.method == "POST":
        articleId = request.data['id']
        userId = request.data['userId']
    if request.method == "GET":
        articleId = request.GET['id']
        userId = request.GET['userId']
    article = Article.objects.get(id=articleId)

    favored = Favourite.objects.filter(belong=article, belong_user_id=userId)

    if favored:
        favored[0].delete()
        return Response({"status": False, "text": "取消收藏"})
    else:
        new_favor = Favourite(belong=article, belong_user_id=userId)
        new_favor.save()
        return Response({"status": True, "text": "收藏成功"})


@api_view(["GET"])
def MyArticle(request):
    id = request.GET["id"]
    articles = Article.objects.filter(belong_id=id).all()
    article_data = []
    for item in articles:
        data = {
            "id": item.id,
            "title": item.title,
            "viewNumber": item.view,
            'date': item.date
        }
        article_data.append(data)
    return Response({"data": article_data})


@api_view(["GET"])
def MyLikeArticle(request):
    id = request.GET["id"]
    articles = Like.objects.filter(belong_user_id=id).all()
    article_data = []
    for item in articles:
        article = Article.objects.filter(id=item.belong_id).first()
        data = {
            "id": item.belong_id,
            "title": article.title,
            "viewNumber": article.view,
            'date': article.date
        }
        article_data.append(data)
    return Response({"data": article_data})


@api_view(["GET"])
def MyFavouriteArticle(request):
    id = request.GET["id"]
    articles = Favourite.objects.filter(belong_user_id=id).all()
    article_data = []
    for item in articles:
        article = Article.objects.filter(id=item.belong_id).first()
        data = {
            "id": item.belong_id,
            "title": article.title,
            "viewNumber": article.view,
            'date': article.date
        }
        article_data.append(data)
    return Response({"data": article_data})
