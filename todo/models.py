from django.db import models

from todo.choices import TodoStatus, TodoPiriority


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=TodoStatus.choices, default=TodoStatus.PENDING)
    priority = models.CharField(max_length=20, choices=TodoPiriority.choices, default=TodoPiriority.Unknown)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
