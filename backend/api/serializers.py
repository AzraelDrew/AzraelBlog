from rest_framework import serializers
from django.contrib.auth.models import User
from api import models


class UserInfoSerializer(serializers.ModelSerializer):
    collects = serializers.SerializerMethodField()
    kudos = serializers.SerializerMethodField()

    class Meta:
        model = models.UserInfo
        fields = "__all__"
        # exclude = ['password']
        read_only_fields = ['user']

    def get_collects(self, obj):
        return CollectSerializer(obj.collect_user.all(), many=True).data

    def get_kudos(self, obj):
        return KudoSerializer(obj.kudo_user.all(), many=True).data

    def to_representation(self, value):
        # 调用父类获取当前序列化数据，value代表每个对象实例ob
        data = super().to_representation(value)
        # 对序列化数据做修改，添加新的数据
        data.pop('password')
        return data


class ArticleSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    collects = serializers.SerializerMethodField()
    kudos = serializers.SerializerMethodField()

    class Meta:
        model = models.Article
        fields = "__all__"

    def get_comments(self, obj):
        return CommentSerializer(obj.comment_article.all(), many=True).data

    def get_collects(self, obj):
        return CollectSerializer(obj.collect_article.all().filter(status=1), many=True).data

    def get_kudos(self, obj):
        return KudoSerializer(obj.kudo_article.all().filter(status=1), many=True).data


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = "__all__"


class CollectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Collect
        fields = "__all__"


class KudoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Kudo
        fields = "__all__"
