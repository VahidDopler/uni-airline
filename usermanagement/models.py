# Create your models here.
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, PermissionsMixin, AbstractUser
from django.db import models


class normal_user(models.Model):
    username = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return f"{self.username}"
