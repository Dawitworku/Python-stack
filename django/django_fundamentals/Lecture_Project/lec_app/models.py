from django.db import models

# Create your models here.
class Dragon(models.Model):
    name = models.CharField(max_length=55)
    has_wings = models.BooleanField()
    fire_color = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Wizard(models.Model):
    name = models.CharField(max_length=45)
    house = models.CharField(max_length=45)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()



class Geocache(models.Model):
    locations = models.CharField(max_length=30)
    treasure = models.TextField()
    dragon = models.ForeignKey(Dragon, related_name='owned_geocaches', on_delete = models.CASCADE)
    dragons_that_found = models.ManyToManyField(Dragon, related_name='found_geocache')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


