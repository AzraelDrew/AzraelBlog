from Blog.models import Article, UserInfo, Lanmu, Pinglun, Like, Favourite
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password, make_password
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User, Group, Permission, ContentType
from django.utils.timezone import localtime

hostUrl = 'http://127.0.0.1:8000/'


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
        UserInfo.objects.get(id=article.belong_id).headImg,
        'belonguser':
        UserInfo.objects.get(id=article.belong_id).nickName,
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
    username = request.POST['username']
    password = request.POST['password']
    # 登录逻辑
    user = User.objects.get(username=username)
    nickName = UserInfo.objects.get(belong_id=user.id).nickName
    desc = UserInfo.objects.get(belong_id=user.id).desc
    phone = UserInfo.objects.get(belong_id=user.id).phone

    if user:
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


@api_view(["POST"])
def GetUserInfo(request):
    if not request.POST['token']:
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
        userinfo = ResUserInfo(request.POST['token'])
    return Response(userinfo)


@api_view(["POST"])
def UpdateUserInfo(request):
    token = request.POST["token"]
    id = CurrentUserId(token)
    name = request.POST["name"]
    nickName = request.POST["nickName"]
    avatar = request.POST["avatar"]
    phone = request.POST["phone"]
    desc = request.POST["desc"]
    User.objects.filter(id=id).update(username=name)
    UserInfo.objects.filter(id=id).update(headImg=avatar,
                                          nickName=nickName,
                                          desc=desc,
                                          phone=phone)
    return Response("ok")


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
    title = request.POST['title']
    describe = request.POST['describe']
    content = request.POST['content']
    token = request.POST["token"]
    id = CurrentUserId(token)
    cover = hostUrl + 'upload/' + 'defaultCover.png'
    user_token = Token.objects.filter(user_id=id).first()
    # 保存文章
    Article.objects.create(title=title,
                           cover=cover,
                           content=content,
                           describe=describe,
                           belong=user_token.user)
    return Response("OK")


@api_view(["POST"])
def UpdateArticle(request):
    articleId = request.POST["articleId"]
    title = request.POST['title']
    describe = request.POST['describe']
    content = request.POST['content']
    token = request.POST["token"]
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
    page = request.GET["page"]
    pageSize = request.GET["pageSize"]
    userId = request.GET['userId']
    if not userId:
        userId = 0
    articles = Article.objects.all().order_by('id')
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
    userinfo = UserInfo.objects.get(id=article.belong_id)
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
            "nickName":
            pinglun.belong_user.username,
            "text":
            pinglun.text,
            'date':
            pinglun.date,
            "avatar":
            UserInfo.objects.filter(id=pinglun.belong_user_id).first().headImg
        }
        pinglun_data.append(pinglun_item)
    return Response({"data": pinglun_data, "total": total})


@api_view(["POST"])
def AddComment(request):
    articleId = request.POST["id"]
    currentId = request.POST["userId"]
    comment = request.POST["text"]

    new_pinglun = Pinglun(belong_user_id=currentId,
                          belong_id=articleId,
                          text=comment)
    new_pinglun.save()
    return Response("OK")


@api_view(['GET', 'POST'])
def ArticleLike(request):

    articleId = request.GET['id']
    userId = request.GET['userId']
    article = Article.objects.get(id=articleId)

    liked = Like.objects.filter(belong=article, belong_user_id=userId)

    if liked:
        liked[0].delete()
        return Response({"status": False})
    else:
        new_like = Like(belong=article, belong_user_id=userId)
        new_like.save()
        return Response({"status": True})


@api_view(['GET', 'POST'])
def ArticleFavor(request):
    articleId = request.GET['id']
    userId = request.GET['userId']
    article = Article.objects.get(id=articleId)

    favored = Favourite.objects.filter(belong=article, belong_user_id=userId)

    if favored:
        favored[0].delete()
        return Response({"status": False})
    else:
        new_favor = Favourite(belong=article, belong_user_id=userId)
        new_favor.save()
        return Response({"status": True})


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