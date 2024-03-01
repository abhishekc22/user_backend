
from django.db import models
from django.contrib.auth.models import AbstractUser

class Member(AbstractUser):
    username=models.CharField(max_length=25,unique=True)
    email=models.EmailField(unique=True)
    PhoneNumber=models.IntegerField(blank=True,null=True)
    Address=models.CharField(max_length=25,null=True)
    DateJoined=models.DateField(blank=True,null=True)

class Class(models.Model):
    Title=models.CharField(max_length=50)
    Description=models.CharField(max_length=50)
    Schedule=models.TimeField()

class Attendance(models.Model):
    user=models.ForeignKey(Member,on_delete=models.CASCADE)
    Class_ID=models.ForeignKey(Class,on_delete=models.CASCADE)
    Date=models.DateField()
    Status =models.BooleanField(blank=False)
