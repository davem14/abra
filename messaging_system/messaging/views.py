from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveDestroyAPIView

from .models import Message
from .serializers import MessageSerializer


class SendMessage(CreateAPIView):
    serializer_class = MessageSerializer


class ReceivedMessage(RetrieveDestroyAPIView):

    serializer_class = MessageSerializer
    lookup_url_kwarg = 'message_id'

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user.id)

    def get_object(self):
        message = super().get_object()
        message.mark_as_read()
        return message


class ReadAllMessages(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Message.objects.filter(receiver=self.request.user.id)
        for message in queryset:
            message.mark_as_read()
        return queryset


class ReadAllUnreadMessages(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Message.objects.filter(receiver=self.request.user.id, read=False)
        for message in queryset:
            message.mark_as_read()
        return queryset
