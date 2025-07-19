import logging
from django.utils import timezone
from datetime import timedelta
from django_ratelimit.decorators import ratelimit
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, OTP
from .serializers import RequestOTPSerializer, VerifyOTPSerializer, UserSerializer

logger = logging.getLogger(__name__)

def generate_otp_code():
    return f"{random.randint(1000, 9999)}"

class RequestOTPView(APIView):
    #limit for requesting 3 otp code in 10 minutes
    @ratelimit(key='post:mobile', rate='3/10m', block=True)
    def post(self, request):
        serializer = RequestOTPSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        mobile = serializer.validated_data['mobile']

        # deleting old opts
        OTP.objects.filter(mobile=mobile, created_at__lt=timezone.now()-timedelta(minutes=5)).delete()

        # generating new otp
        code = generate_otp_code()
        OTP.objects.create(mobile=mobile, code=code)
        print(f"OTP for {mobile}: {code}")  #printing opt code instead of sending using sms

        return Response({"detail": "OTP sent successfully (check logs)."}, status=status.HTTP_200_OK)
    
