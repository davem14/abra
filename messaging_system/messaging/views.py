from rest_framework.views import APIView


class WriteMessage(APIView):

    def post(self, request):
        pass


class ReadMessage(APIView):

    def get(self, request):
        pass


class ReadAllMessages(APIView):

    def get(self, request):
        pass


class ReadAllUnreadMessages(APIView):

    def get(self, request):
        pass


class DeleteMessage(APIView):

    def delete(self, request):
        pass
