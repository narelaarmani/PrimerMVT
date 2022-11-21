from django.db import models

# Create your models here.

class Family(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fechanac = models.DateField()

class Friends(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    