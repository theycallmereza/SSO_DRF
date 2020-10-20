from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.
class HelloView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        print(request.user.username)
        content = {'message': f'Hello!'}
        return Response(content)
