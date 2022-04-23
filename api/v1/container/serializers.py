from rest_framework import serializers

from product.models import Container


class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = '__all__'
