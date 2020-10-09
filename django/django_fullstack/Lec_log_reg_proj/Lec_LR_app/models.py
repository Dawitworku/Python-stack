from django.db import models
import re
# Create your models here.


class UserManager(models.Manager):
    def create_validator(self, postData):
        errors = {}

        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['user_name']) < 5:
            errors['user_name'] = "User Name should be 5 characters"

        if len(postData['email']) < 8:
            errors['email'] = "Email should be Longer"

        if len(postData['password']) < 8:
            errors['password'] = "Password should Longer"

        if postData['password'] != postData['password_conf']:
            errors['password_conf'] = "Password and password conf need to match"

        if not EMAIL_REGEX.match(postData['email']):
            errors['regex'] = "Invalid email address"
        return errors


class KoalaManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        if len(postData['koala_name']) < 3:
            errors['koala_name'] = "Koala Name is to short"

        if len(postData['talent']) < 6:
            errors['talent'] = "Talent is too short."

        Koalas_with_same_name = Koala.objects.filter(name=postData['koala_name'])
        if len(Koalas_with_same_name) > 0:
            errors['duplicate'] = "Name already taken. Pick another one."
        return errors


class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Koala(models.Model):
    name = models.CharField(max_length=40)
    talent = models.TextField()
    user = models.ForeignKey(User, related_name='koalas', on_delete=models.CASCADE)
    users_votes = models.ManyToManyField(User, related_name='voted_koalas')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = KoalaManager()
