from django.db import models

# Create your models here.
class registrationform(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    place=models.CharField(max_length=30)
    profile=models.ImageField(upload_to='media/')
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class gallery(models.Model):
     brand=models.CharField(max_length=30)
     name=models.CharField(max_length=40)
     photo=models.ImageField(upload_to='media/',null=True,blank=True)
     rate=models.IntegerField()
    
