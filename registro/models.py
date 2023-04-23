from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CategoriaUser(models.Model):
    type=models.CharField(max_length=100)

class UserPersonalizado(AbstractUser):
    type=models.ForeignKey(CategoriaUser,verbose_name='types',default=1,on_delete=models.CASCADE)