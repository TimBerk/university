from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class IndexView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        data = {'test': 'Courses base API'}
        return Response(data)
