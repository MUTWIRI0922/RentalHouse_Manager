from django.shortcuts import render

# Create your views here.

from .models import CustomUser
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CustomUserSerializer

class RegisterApiView(generics.CreateApiView)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()






