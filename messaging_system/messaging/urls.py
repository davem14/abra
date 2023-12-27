from django.urls import path

from .views import SendMessage, ReadAllMessages, ReceivedMessage, ReadAllUnreadMessages

urlpatterns = [
    path('send', SendMessage.as_view(), name='send'),
    path('<int:message_id>', ReceivedMessage.as_view(), name='received'),
    path('all', ReadAllMessages.as_view(), name='receive_all'),
    path('unread', ReadAllUnreadMessages.as_view(), name='receive_unread'),
]

