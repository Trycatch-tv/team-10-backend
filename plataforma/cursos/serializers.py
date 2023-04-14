from rest_framework import serializers
from .models import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        read_only_fields = ('created',)
        

        
class CursoSerializer(serializers.ModelSerializer):
    #estudiante = serializers.PrimaryKeyRelatedField(queryset=Estudiante.objects.all(),many=True)
    class Meta:
        model = Curso
        fields = ('title','description','tutor','categoria','fechaInicio','fechaFinalizacion') 
        read_only_fields = ('created_at',)                    

class EstudianteSerializer(serializers.ModelSerializer):
    #curso = serializers.PrimaryKeyRelatedField(queryset=Curso.objects.all(),many=True)
    
    class Meta:
        model = Estudiante
        fields = ('nombre','email')
        read_only_fields = ('created_at',) 
        
    def create(self, validated_data):
        estudiante = Estudiante.objects.create(**validated_data)
        return estudiante     