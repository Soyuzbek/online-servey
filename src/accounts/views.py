from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.apis import *
from accounts.services import *
from common.schemas.accounts import *


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    schema = LoginSchema()

    def post(self, request):
        """
            Login for user.
        """
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token, _ = TokenService.create_auth_token(
            email=serializer.validated_data.get('email'),
            password=serializer.validated_data.get('password')
        )
        return Response(data={
            'message': 'You have successfully logged in',
            'data': {
                'token': str(token),
                'token_type': 'Token',
                'user_id': user.pk
            },
            'status': "OK"
        }, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        """
            Logout for user.
            headers - Authorization Token <token key>
        """
        TokenService.destroy_auth_token(user=request.user)
        return Response(data={
            'message': 'You have successfully logged out',
            'status': "NO CONTENT",
        }, status=status.HTTP_204_NO_CONTENT)


class RegisterAPIView(APIView):
    permission_classes = (AllowAny,)
    schema = RegisterSchema()

    def post(self, request, *args, **kwargs):
        """
            Register for user.
        """
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        UserService.create_user(email=serializer.validated_data.get('email'),
                                password=serializer.validated_data.get('password'),
                                conf_password=serializer.validated_data.get('confirm_password'),
                                is_active=True)
        return Response(data={
            'message': 'The user has successfully registered',
            'status': 'CREATED'
        }, status=status.HTTP_201_CREATED)
