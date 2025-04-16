from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
