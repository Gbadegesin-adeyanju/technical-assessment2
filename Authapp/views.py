from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from django.contrib import auth
from .serializers import UserSerializers, LoginSerializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

# Create your views here.


class RegisterViewset(APIView):

    serializer_class = UserSerializers
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()

    @swagger_auto_schema(request_body=UserSerializers)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = User.objects.create_user(**serializer.validated_data)
            user.is_active = True
            user.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(request_body=LoginSerializers)
    def post(self, request):
        serializer = LoginSerializers(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        user = auth.authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class profileViewset(APIView):

    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            