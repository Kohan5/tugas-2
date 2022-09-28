from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class TaskTodolist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.TextField()
    description = models.TextField()
    is_finished = models.BooleanField()