from rest_framework import serializers

from crud.models import File, Photo, Product



class ProductSer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PhotoSer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class FileSer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
