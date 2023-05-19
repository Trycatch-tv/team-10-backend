from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password 
from .models import *
       

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
    
    
class UserLogin(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    password = serializers.CharField(
        min_length=8, write_only=True)
    
    
    
    class Meta:
        model = get_user_model()
        fields = ('email',  'password')



