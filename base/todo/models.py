from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=300)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    