from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from drf_yasg.utils import swagger_auto_schema

from product.models import Container
from .serializers import ContainerSerializer


class ContainerViewset(viewsets.ModelViewSet):
    serializer_class = ContainerSerializer
    queryset = Container.objects.all()
    authentication_classes = []
    permission_classes = [AllowAny]
