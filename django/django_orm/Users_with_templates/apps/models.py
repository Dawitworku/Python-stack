from django.db import models

# Create your models here.



class User_manager(models.Manager):

    def basic_validator(self, postData):  
        errors = {}
        if len(postData['first_name']) < 1:
            errors['first_name'] = "Please insert your First Name" 

        if len(postData['last_name']) < 1:
            errors['last_name'] = "Please insert your Last Name" 
        
        if len(postData['email']) < 1:
            errors['email'] = "Email Required"
        
        if len(postData['age']) < 1:
            errors['age'] = "Please insert your Age"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=55)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = User_manager()
