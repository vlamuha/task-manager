from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255)


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


class TaskType(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField(editable=True)
    is_completed = models.BooleanField()
    PRIORITY_CHOICES = [
        ("low", "Low Priority"),
        ("medium", "Medium Priority"),
        ("high", "High Priority"),
        ("urgent", "Urgent Priority")
    ]
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=10)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker, related_name="tasks")
