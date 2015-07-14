from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Listing(models.Model):
    info = models.CharField(max_length=200)

class Rating(models.Model):    
	comment = models.CharField(max_length=200)
	rating = models.IntegerField(default=0)
	rater =  models.ForeignKey(User)