from django.urls import re_path
from django.conf.urls import include


urlpatterns = [
    re_path(r'order/', include('api.v1.order.urls')),
    re_path(r'container/', include('api.v1.container.urls')),
]
