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

