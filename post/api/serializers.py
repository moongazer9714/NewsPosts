from rest_framework.serializers import ModelSerializer
from post.models import Post
from rest_framework import serializers

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'photo', 'category',)


