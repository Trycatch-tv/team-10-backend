from rest_framework import serializers
from .models import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        read_only_fields = ('created',)
        
class DomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domicilio
        fields = '__all__'
        
class CursoSerializer(serializers.ModelSerializer):
    #estudiante = serializers.PrimaryKeyRelatedField(queryset=Estudiante.objects.all(),many=True)
    class Meta:
        model = Curso
        fields = ('title','description','tutor','estudiante','categoria',) 
        read_only_fields = ('created_at',)                    

class EstudianteSerializer(serializers.ModelSerializer):
    #curso = serializers.PrimaryKeyRelatedField(queryset=Curso.objects.all(),many=True)
    domicilio= DomicilioSerializer(required=True)
    #domicilio = serializers.StringRelatedField(queryset=Domicilio.objects.filter(id),many=False)
    class Meta:
        model = Estudiante
        fields = ('nombre','apellido','dni','telefono','email','domicilio')
        read_only_fields = ('created_at',) 
        
    def create(self, validated_data):
        domicilio_data = validated_data.pop('domicilio')
        estudiante = Estudiante.objects.create(**validated_data)
        #for domicilio in domicilio_data:
        Domicilio.objects.create(estudiante=estudiante, **domicilio_data)
        return estudiante     