from rest_framework import serializers
from .models import User

class RequestOTPSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=15)

class VerifyOTPSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=15)
    code = serializers.CharField(max_length=6)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['mobile', 'date_joined']