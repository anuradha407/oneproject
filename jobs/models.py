from django.db import models

# Create your models here.
class Job(models.Model):
    image=models.ImageField(upload_to='images/')
    summary= models.CharField(max_length=300)
class Post(models.Model):
    first_name= models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
