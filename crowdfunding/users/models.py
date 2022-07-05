from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # id = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200)

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

    def __str__(self):
        return self.username
