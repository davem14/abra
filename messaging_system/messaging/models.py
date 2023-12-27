from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL)
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL)
    message = models.TextField()
    subject = models.CharField(max_length=256)
    creation_date = models.DateField(auto_now_add=True)
    read = models.BooleanField(default=False)
