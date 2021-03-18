from rest_framework import generics, request
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from main.models import Post, Like
from main.permissions import IsOwnerOrReadOnly
from main.serializers import PostDetailSerializer, PostListSerializer


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostDetailSerializer


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)


class LikeAnalyticsView(generics.ListAPIView):
    lowest_date = '2020-01-01'
    highest_date = '2100-01-01'

    start_date = request.GET.get('date__gte', lowest_date)

    end_date = request.GET.get('date__lte', highest_date)

    queryset = Like.objects.filter(article_date_published__gte=start_date,
                                      article_date_published__lte=end_date)


