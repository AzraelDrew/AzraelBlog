from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from api import models, serializers


class ArticleView(ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer

    def retrieve(self, request, pk, *args, **kwargs):
        article = self.queryset.filter(pk=pk).first()
        print(article)
        if request.GET.get('key') == "view":
            article.view = article.view+1
            article.save()
            return Response(self.serializer_class(article).data)
        return Response(self.serializer_class(article).data)
