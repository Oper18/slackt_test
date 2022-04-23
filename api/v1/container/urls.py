from django.urls import re_path

from .views import ContainerViewset


urlpatterns = [
    re_path(r'products/$', ContainerViewset.as_view({
        'get': 'list',
        'post': 'create',
    })),
    re_path(r'product/(?P<pk>\d+)/$', ContainerViewset.as_view({
        'put': 'update',
        'delete': 'destroy'
    })),
]
