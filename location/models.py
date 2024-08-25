from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField()
    name = models.TextField(max_length=50)
    email = models.EmailField()
    # image = models.ImageField()

class Location(models.Model):
    id = models.AutoField()
    name = models.TextField()
    description = models.TextField()    

