from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from api import models, serializers
from api.utils.password import Password


class UserView(Password):
    queryset = models.UserInfo.objects.all()
    serializer_class = serializers.UserInfoSerializer

    def perform_create(self, serializer):
        try:
            username = serializer.validated_data['username']
            hashPassword = self.MakePassword(serializer.validated_data)
            user = User.objects.create(
                username=username, password=hashPassword)
            serializer.validated_data['password'] = hashPassword
            serializer.validated_data['user'] = user
        except Exception as ex:
            return Response({"Error": str(ex)})
        Token.objects.create(user=user)
        serializer.save()

    def perform_update(self, serializer):
        serializer.validated_data['password'] = self.MakePassword(
            serializer.validated_data)
        User.objects.filter(username=serializer.validated_data['username']).update(
            username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        serializer.save()


class LoginView(Password):
    queryset = models.UserInfo.objects.all()
    serializer_class = serializers.UserInfoSerializer

    def login(self, request, *args, **kwargs):
        username = request.data['username']
        userinfo = self.queryset.filter(username=username).first()
        userId = User.objects.get(username=username).id
        if userinfo and self.AuthPassword(request.data, userinfo.password):
            data = self.serializer_class(userinfo, many=False).data
            data['token'] = Token.objects.get_or_create(user_id=userId)[0].key
            return Response(data)
        return Response({"message": "用户不存在 或  密码错误"})


class TokenView(APIView):
    def post(self, request):
        token = Token.objects.filter(**request.data).first()
        if token:
            userInfo = models.UserInfo.objects.filter(
                user_id=token.user_id).first()
            data = serializers.UserInfoSerializer(userInfo).data
            data['token'] = token.key
            return Response(data)
        else:
            return Response({"message": "token已失效"})
