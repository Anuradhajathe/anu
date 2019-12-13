from django.db import models

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=20)
    sage = models.IntegerField()
    scity = models.CharField(max_length=20)
    sdes= models.CharField(max_length=20)
