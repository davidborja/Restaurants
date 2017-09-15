from django.db import models

# Create your models here.

#Modelo Restaurants
 
class Restaurants (models.Model):
 rating= models.IntegerField() #INTEGER, -- Number between 0 and 4
 name=models.CharField(max_length=100) #TEXT -- Name of the restaurant
 site=models.CharField(max_length=100) #TEXT -- Url of the restaurant
 email=models.CharField(max_length=100) #TEXT,
 phone=models.CharField(max_length=100) #TEXT
 street=models.CharField(max_length=100) #TEXT
 city=models.CharField(max_length=100) #TEXT
 state=models.CharField(max_length=100) #TEXT
 lat=models.FloatField() #FLOAT -- Latitude
 lng=models.FloatField() #FLOAT -- Longitude




