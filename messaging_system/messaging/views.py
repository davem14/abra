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


class ReadAllMessages(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user.id)


class ReadAllUnreadMessages(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user.id, read=False)
