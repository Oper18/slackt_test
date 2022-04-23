from django.contrib import admin

from .models import Container


class ContainerAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'size')

admin.site.register(Container, ContainerAdmin)
