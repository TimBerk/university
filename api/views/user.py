from django.middleware.csrf import get_token
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view

from api.serializers.user import UserDetailSerializer, LoginSerializer


class UserDetailView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        current_user = request.user
        serializer = UserDetailSerializer(current_user)
        return Response(serializer.data)


class LoginView(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.login(data=data, request=request)

        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('POST',))
def logout_view(request):
    """Blacklist the refresh token: extract token from the header
      during logout request user and refresh token is provided"""
    refresh_token = request.data.get('token', None)
    if refresh_token:
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response("Successful Logout", status=status.HTTP_200_OK)
    return Response("Incorrect token", status=status.HTTP_400_BAD_REQUEST)


@api_view(('POST',))
def get_csrf(request):
    csrf_token = get_token(request)
    return Response({'csrf_token': csrf_token})
