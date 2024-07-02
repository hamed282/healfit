from rest_framework import serializers
from .models import BlogModel


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'


class BlogAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ['cover_image', 'title', 'slug']


# class BlogLandSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BlogModel
#         fields = ['cover_image', 'title', 'slug']
