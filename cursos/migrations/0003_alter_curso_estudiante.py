# Generated by Django 4.2 on 2023-04-09 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_remove_curso_imagen_remove_estudiante_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='estudiante',
            field=models.ManyToManyField(null=True, to='cursos.estudiante'),
        ),
    ]
