from django.db import models


class TodoStatus(models.TextChoices):
    PENDING = "p", "Pending"
    DONE = "d", "Done"
    CANCELED = "c", 'Canceled'
    IN_PROGRESS = "i", 'In Progress'


class TodoPriority(models.TextChoices):
    LOW = "l", "Low"
    MEDIUM = "m", "Medium"
    HIGH = "h", "High"
    Urgent = "ur", "Urgent"
