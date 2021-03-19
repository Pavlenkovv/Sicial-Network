from django.db.models import Count
from django.db.models.functions import TruncDate
from rest_framework import generics, viewsets, response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from main.models import Post, Like
from main.permissions import IsOwnerOrReadOnly
from main.serializers import PostEditSerializer, PostListSerializer, PostSerializer, \
    LikeAnalyticsView


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostEditSerializer


class PostView(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=["post"])
    def like(self, request, pk=None):
        if len(Like.objects.filter(user_id=request.user.id, post_id=self.get_object().id)) > 0:
            return response.Response({"status": "post is already liked"})
        like = Like(user_id=request.user, post_id=self.get_object())
        like.save()
        return response.Response({"status": "post liked"})

    @action(detail=True, methods=["post"])
    def unlike(self, request, pk=None):
        like = Like.objects.filter(user_id=request.user.id, post_id=self.get_object().id)
        if len(like) == 0:
            return response.Response({"status": "post wasn't liked"})
        like[0].delete()
        return response.Response({"status": "post unliked"})


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)


class PostEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostEditSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)


class LikeAnalyticsView(generics.ListAPIView):
    serializer_class = LikeAnalyticsView
    queryset = Like.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        lowest_date = '2020-01-01'
        highest_date = '2100-01-01'
        start_date = self.request.GET.get('date_from', lowest_date)
        end_date = self.request.GET.get('date_to', highest_date)
        queryset = Like.objects \
            .filter(creation_date__gte=start_date, creation_date__lte=end_date) \
            .annotate(date=TruncDate('creation_date')) \
            .values('date') \
            .annotate(likes=Count('id'))
        return queryset
