from rest_framework import serializers

from crud.models import Product



class ProductSer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PhotoSer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class FileSer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
