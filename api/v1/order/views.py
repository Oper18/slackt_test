from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from drf_yasg.utils import swagger_auto_schema

from order.models import Order
from .serializers import OrderSerializer


class OrderViewset(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    authentication_classes = []
    permission_classes = [AllowAny]
