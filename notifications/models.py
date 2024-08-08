# myapp/models.py

from django.db import models
from django.contrib.auth.models import User
from .utils import send_notifications

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

class SomeModel(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        send_notifications(user_id=1, message="A model instance has been created or updated")
