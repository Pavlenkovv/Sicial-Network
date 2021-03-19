from django.urls import path
from rest_framework.routers import DefaultRouter

from main.views import *

router = DefaultRouter()
router.register(r'post', PostView)

urlpatterns = [
    path('post/create/', PostCreateView.as_view()),
    path('all/', PostListView.as_view()),
    path('post/edit/<int:pk>/', PostEditView.as_view()),
]
urlpatterns += router.urls
