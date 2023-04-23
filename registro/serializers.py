from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserPersonalizado,CategoriaUser
#User=get_user_model()

class CategoriaSerializer(serializers.ModelSerializer):
    #id=serializers.ReadOnlyField()
    type=serializers.CharField()
    class Meta:
        model=CategoriaUser
        fields='__all__'
    

class UserSerializer(serializers.ModelSerializer):
    #id= serializers.ReadOnlyField()
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    #type=serializers.IntegerField()
    type = serializers.PrimaryKeyRelatedField(queryset=CategoriaUser.objects.all())
    class Meta:
        model = UserPersonalizado
        fields = ('first_name','last_name','email','password','type')
         
    
    def create (self, validate_data):
        instance=UserPersonalizado()
        instance.first_name=validate_data.get('first_name')
        instance.last_name=validate_data.get('last_name')
        instance.email=validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.type=validate_data.get('type')
        instance.save()
        return instance
    
    def validate_email(self,data):
        users=UserPersonalizado.objects.filter(email=data)
        if len(users) !=0:
            raise serializers.ValidationError('Email existente, ingrese uno nuevo')
        else:
            return data