from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password 
from .models import RoleGroup






class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8, write_only=True)
    rol = serializers.CharField(
        required=True)
    
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password', 'rol')

    def validate_password(self, value):
        return make_password(value)
    


class UserLogin(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    password = serializers.CharField(
        min_length=8, write_only=True)
    
    
    
    class Meta:
        model = get_user_model()
        fields = ('email',  'password')

class RoleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleGroup
        fields = ('id', 'name', 'description')

        






