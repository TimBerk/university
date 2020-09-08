from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers.user import UserDetailSerializer, LoginSerializer


class UserDetailView(APIView):

    def get(self, request):
        current_user = request.user
        serializer = UserDetailSerializer(current_user)
        return Response(serializer.data)


class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.login(data=data, request=request)

        return Response(serializer.data, status=status.HTTP_200_OK)
