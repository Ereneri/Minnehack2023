from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from datetime import date

User=get_user_model()

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
