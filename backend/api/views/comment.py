from rest_framework.viewsets import ModelViewSet
from api import models, serializers
from api.utils.pagination import PageNumberPagination


class ComentView(ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        if request.GET.get('articleId'):
            self.queryset = self.queryset.filter(
                relate_article=request.GET['articleId'])
        return super().list(request, *args, **kwargs)
