from django.urls import re_path

from .views import OrderViewset


urlpatterns = [
    re_path(r'orders/$', OrderViewset.as_view({
        'get': 'list',
        'post': 'create',
    })),
    re_path(r'order/(?P<pk>\d+)/$', OrderViewset.as_view({
        'put': 'update',
        'delete': 'destroy'
    })),
]
