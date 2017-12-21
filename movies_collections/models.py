from django.db import models

# Create your models here.
class Movies(models.Model):
	language=models.CharField(max_length=250,blank=True)
	movie_name=models.CharField(max_length=250,blank=True)
	typeofmovie=models.CharField(max_length=250,blank=True)
	releaseyear=models.CharField(max_length=250,blank=True)
