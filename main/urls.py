from django.urls import path

from main.views import *

urlpatterns = [
    path('post/create/', PostCreateView.as_view()),
    path('all/', PostListView.as_view()),
    path('post/detail/<int:pk>/', PostDetailView.as_view()),
]