from rest_framework import serializers
from .models import Curso, Estudiante

# definiendo los serializadores de Django REST Framework

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'
