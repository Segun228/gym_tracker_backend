from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import AppUserSerializer
from .handle_sign import handle_sign
from django.http import HttpResponseForbidden
from .models import AppUser
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.views import TokenRefreshView
import logging


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = AppUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


logger = logging.getLogger(__name__)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('VK '):
            logger.error('Missing or invalid VK authorization header')
            return HttpResponseForbidden(
                "Invalid authorization header format. Expected 'VK <base64_data>'",
                status=status.HTTP_403_FORBIDDEN
            )


        encoded_json = auth_header[3:]
        print(encoded_json)
        vk_data = handle_sign(encoded_json)
        
        if not vk_data:
            logger.error('VK signature verification failed')
            return HttpResponseForbidden(
                "Invalid VK signature or expired token",
                status=status.HTTP_403_FORBIDDEN
            )


        required_fields = ['vk_user_id', 'vk_ts', 'vk_app_id']
        if not all(field in vk_data for field in required_fields):
            logger.error(f'Missing required fields in VK data: {vk_data}')
            return HttpResponseForbidden(
                "Missing required authentication data",
                status=status.HTTP_403_FORBIDDEN
            )


        try:
            user, created = AppUser.objects.get_or_create(
                vk_user_id=vk_data['vk_user_id'],
                defaults={
                    'username': vk_data.get('vk_name', f"vk_user_{vk_data['vk_user_id']}"),
                    'first_name': vk_data.get('vk_first_name', ''),
                    'last_name': vk_data.get('vk_last_name', ''),
                }
            )
            

            if not created:
                user.username = vk_data.get('vk_name', user.username)
                user.save()

        except Exception as e:
            logger.error(f'User creation failed: {str(e)}')
            return Response(
                {"error": "User authentication failed"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        return Response({
            "access": str(access),
            "refresh": str(refresh),
            "user_id": user.id,
            "is_new_user": created
        }, status=status.HTTP_200_OK)


class RefreshView(TokenRefreshView):
    permission_classes = [AllowAny]



class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = AppUserSerializer(request.user)
        return Response(serializer.data)