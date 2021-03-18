from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from main.models import Post
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
