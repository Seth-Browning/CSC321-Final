from rest_framework import serializers
from forum.models import Thread, Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at']

class ThreadSerializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Thread
        fields = ['id', 'category', 'title', 'creator', 'created_at', 'posts']

class ThreadSerializer_NoPosts(serializers.ModelSerializer):
    creator = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Thread
        fields = ["id", "category", "title", "creator", "created_at"]