from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter

class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginSerializers(serializers.Serializer):
    username = serializers.CharField(max_length = 150, required=True)
    password = serializers.CharField(max_length=128, write_only=True, required=True)

