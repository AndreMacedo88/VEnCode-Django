from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager


# Create your models here.

class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()
