from django.contrib.auth.models import AbstractUser, Group
from django.db import models




class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True, auto_created=True)
    cedula = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=150, unique=True)
    phone = models.CharField(max_length=20, null=True)
    rol = models.CharField(max_length=50, null=True, blank=False)
    

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['id', 'username', 'cedula', 'phone', 'password', 'rol']




    def __str__(self):
        return self.username


class RoleGroup(Group):
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Group'

    def __str__(self):
        return self.name