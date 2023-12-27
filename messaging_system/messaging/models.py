from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    sender = models.ForeignKey(User, null=True, related_name='sent_messages', on_delete=models.SET_NULL)
    receiver = models.ForeignKey(User, null=True, related_name='received_messages', on_delete=models.SET_NULL)
    message = models.TextField()
    subject = models.CharField(max_length=256)
    creation_date = models.DateField(auto_now_add=True)
    read = models.BooleanField(default=False)
