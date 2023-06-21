from django.db import models


class Position:
    name = models.CharField(max_length=255)
