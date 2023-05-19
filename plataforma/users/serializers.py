from authentication.serializers import *
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

class RoleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleGroup
        fields = ('id', 'name', 'description')


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'rol')

