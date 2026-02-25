from .models import CustomUser
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token




class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']

        )
        return user

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        print(data)
        user = authenticate(
            username=data.get('username'), 
            password=data.get('password')
        )
        if user is None:
            raise serializers.ValidationError('Invalid username or password')
        token, created = Token.objects.get_or_create(user=user)
        return {
            "token": token.key,
            "username": user.username,
            "is_manager": user.is_manager,
            "is_admin": user.is_admin
        
        }