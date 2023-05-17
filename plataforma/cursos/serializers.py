from rest_framework import serializers
from .models import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        read_only_fields = ('created',)
        


class CursoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Curso
        fields = ('id','nombre','descripcion','profesor','categoria','fechaInicio','fechaFinalizacion') 
        read_only_fields = ('created_at',)                    

"""class RegistrarseCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrarseCurso
        fields = ('nombre','estudiante')
        read_only_fields = ('created_at',)          """          
