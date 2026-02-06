import random

from django.conf import settings
from django.core.cache import cache
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import OTPRequestSerializer, OTPVerifySerializer, UserSerializer


def _otp_cache_key(phone_number: str) -> str:
    return f"otp:{phone_number}"


class RequestOTPView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = OTPRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data["phone_number"]
        otp = f"{random.randint(0, 999999):06d}"
        cache.set(_otp_cache_key(phone_number), otp, timeout=300)

        User.objects.get_or_create(phone_number=phone_number)

        payload = {"message": "OTP sent"}
        if settings.DEV_OTP_BYPASS:
            payload["otp"] = otp
        return Response(payload, status=status.HTTP_200_OK)


class VerifyOTPView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = OTPVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data["phone_number"]
        otp = serializer.validated_data["otp"]
        cached = cache.get(_otp_cache_key(phone_number))

        if not cached or cached != otp:
            return Response({"detail": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(phone_number=phone_number)
        refresh = RefreshToken.for_user(user)
        return Response(
            {"access": str(refresh.access_token), "refresh": str(refresh)},
            status=status.HTTP_200_OK,
        )


class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)
