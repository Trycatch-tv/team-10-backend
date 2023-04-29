from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password 
from .models import *



class RoleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleGroup
        fields = ('id', 'name', 'description')

        

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField(required=True)
    cedula = serializers.IntegerField(required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.IntegerField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    rol = serializers.CharField(required=True)
    
    
    class Meta:
        model = get_user_model()
        fields = ( 'id', 'username', 'cedula', 'email', 'phone', 'password', 'rol')

    def validate_password(self, value):
        return make_password(value)
    
    """def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            cedula=validated_data['cedula'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            password=validated_data['password'],
            rol=validated_data['rol']
        )
        return user"""

class UserLogin(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    password = serializers.CharField(
        min_length=8, write_only=True)
    
    
    
    class Meta:
        model = get_user_model()
        fields = ('email',  'password')









class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'rol')
