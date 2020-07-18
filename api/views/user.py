from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers.user import UserDetailSerializer


class UserDetailView(APIView):

    def get(self, request):
        current_user = request.user
        serializer = UserDetailSerializer(current_user)
        return Response(serializer.data)
