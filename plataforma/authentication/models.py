from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=150, unique=True)
    rol = models.CharField(max_length=50, null=True, blank=True)
    

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password', 'rol']


class RoleGroup(Group):
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Group'

    def __str__(self):
        return self.name