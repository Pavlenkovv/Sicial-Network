from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.CharField(db_index=True, max_length=255, unique=True, null=False, blank=False)
    text = models.TextField(max_length=1000, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveSmallIntegerField(default=0)
    dislikes = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
