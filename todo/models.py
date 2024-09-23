from django.db import models
from django.conf import settings
from todo.choices import TodoStatus, TodoPriority


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=TodoStatus.choices, default=TodoStatus.PENDING)
    priority = models.CharField(max_length=20, choices=TodoPriority.choices, default=TodoPriority.MEDIUM)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
