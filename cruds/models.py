from django.db import models

# Create your models here.
class comments(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    email = models.EmailField(max_length=40)
    text = models.TextField(max_length=100)
    # date = models.CharField(max_length=30)

class movies(models.Model):
    title = models.CharField(max_length=40, primary_key=True)
    plot = models.TextField(max_length=100)
    year = models.IntegerField()
    rated = models.CharField(max_length=20)

class users(models.Model):
    name = models.CharField(max_length=25, primary_key=True)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=100)

