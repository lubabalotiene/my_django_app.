
from django.contrib import admin
from django.db import models

class my_new_combrate(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    supporters = models.ManyToManyField('Supporter', related_name='supported_my_new_combrate')

    def __str__(self):
        return self.name

class Supporter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
