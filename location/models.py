from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50)
    email = models.EmailField()
    blogs_id = models.TextField()
    # image = models.ImageField()

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()    
    rating = models.IntegerField(null=True,validators=[MinValueValidator(1), MaxValueValidator(5)])

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()    
    rating = models.IntegerField(null=True,validators=[MinValueValidator(1), MaxValueValidator(5)])
    location_id = models.IntegerField()
    blog_id = models.IntegerField(null=True)

class Tourist_spot(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()    
    rating = models.IntegerField(null=True,validators=[MinValueValidator(1), MaxValueValidator(5)])
    location_id = models.IntegerField()
    blog_id = models.IntegerField(null=True)

class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()    
    rating = models.IntegerField(null=True,validators=[MinValueValidator(1), MaxValueValidator(5)])
    location_id = models.IntegerField()
    restaurant_id = models.IntegerField()
    blog_id = models.IntegerField(null=True)

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField()    
    blog_type =models.IntegerField(null=True,validators=[MinValueValidator(1), MaxValueValidator(4)])
    #1 - Location, 2- Tourist_spot, 3- Hotel, 4- Restaurant
    subject_id = models.IntegerField(null=True)
    likes = models.IntegerField(null=True)
    user_id = models.IntegerField()

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField()    
    review_type =models.IntegerField(null=True,validators=[MinValueValidator(1), MaxValueValidator(4)])
    #1 - Location, 2- Tourist_spot, 3- Hotel, 4- Restaurant
    subject_id = models.IntegerField(null=True)
    likes = models.IntegerField(null=True)
    user_id = models.IntegerField()
    

# class Meta:
#     db_table = 'location'