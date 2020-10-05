from django.db import models

from datetime import datetime, date
# Create your models here.

class ShowManager(models.Manager):
    def show_validator(self, postData):
        errors = {}

        if len(postData['title']) < 2:
            errors['title'] = "Title should be at least 2 characters"

        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters"

        # if datetime.datetime.strptime(postData['release_date'], '%Y-%m-%d').strftime('%Y-%m-%d') > datetime.datetime.strptime(datetime.datetime.today(), '%Y-%m-%d').strftime('%Y-%m-%d'):

        # if no date given or if the date is a future date, throw the error.
        if postData['release_date'] == '' or datetime.strptime(postData["release_date"], '%Y-%m-%d') > datetime.today() :
            print(datetime.today())
            errors['release_date'] = "Release should be in the past"
            
        # if we have any description, it should be at least 10 characters.
        if postData['description'] != '' and len(postData['description']) < 10:
            errors['description'] = "Description should be at least 10 characters"

        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=55)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

