from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    nickname = models.CharField(max_length=64)
    age = models.PositiveIntegerField(default=0)

