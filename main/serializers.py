from rest_framework import serializers

from main.models import Post, Like


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostEditSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = '__all__'


class LikeAnalyticsView(serializers.ModelSerializer):
    date = serializers.DateField()
    likes = serializers.IntegerField()

    class Meta:
        model = Like
        fields = ('date', 'likes')
