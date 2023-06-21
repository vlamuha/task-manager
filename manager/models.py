from django.contrib.auth.models import AbstractUser
from django.db import models


class Position:
    name = models.CharField(max_length=255)


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
