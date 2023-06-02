from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from api import models, serializers


class CollectView(ModelViewSet):
    queryset = models.Collect.objects.all()
    serializer_class = serializers.CollectSerializer

    def collect(self, request, *args, **kwargs):
        if self.queryset.filter(**request.data).exists():
            if self.queryset.filter(**request.data).first().status:
                self.queryset.filter(**request.data).update(status=0)
                return Response(self.serializer_class(self.queryset.filter(**request.data).first(), many=False).data)

            else:
                self.queryset.filter(**request.data).update(status=1)
                return Response(self.serializer_class(self.queryset.filter(**request.data).first(), many=False).data)
        else:
            return super().create(request, *args, **kwargs)
