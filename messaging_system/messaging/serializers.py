from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Message


class MessageSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        message = Message(
            sender=User.objects.get(username=validated_data['sender']),
            receiver=User.objects.get(username=validated_data['receiver']),
            subject=validated_data['subject'],
            message=validated_data['message'],
        )
        message.save()
        return message

    def update(self, instance, validated_data):
        instance.read = True

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'subject', 'message', 'id', 'creation_date']
        read_only_fields = ['id', 'creation_date']
