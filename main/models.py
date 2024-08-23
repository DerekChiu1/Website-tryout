from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 128)
    rank = models.IntegerField()
    location = models.CharField(max_length = 1024)
    campus_size = models.IntegerField()

class Country(models.Model):
    name = models.CharField(max_length = 128)
    population = models.IntegerField()
    location = models.CharField(max_length = 1024)
    land_size = models.IntegerField()

class Person(models.Model):
    name = models.CharField(max_length = 128)
    profession = models.CharField(max_length = 128)
    income = models.IntegerField()
    age = models.IntegerField()

