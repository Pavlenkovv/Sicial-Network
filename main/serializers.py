from rest_framework import serializers

from main.models import Post, Like


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = '__all__'


class LikeAnalyticsView(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
