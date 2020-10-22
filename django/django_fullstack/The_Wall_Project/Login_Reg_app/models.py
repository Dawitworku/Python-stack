from django.db import models
import re
from datetime import datetime, date
# Create your models here.

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}

        Name_REGEX = re.compile(r'^[a-zA-Z.+_-]+$')
        email_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        # Validating the length of users first name
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First Name should be at least 2 characters."

        # Validating users first name and ensuring its only Letters
        if not Name_REGEX.match(postData['first_name']):
            errors['first_name'] = "Invalid first name."

        # Validating the length of users last name
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name should be at least 2 characters."

        # Validating users last name and ensuring its only Letters
        if not Name_REGEX.match(postData['last_name']):
            errors['last_name'] = "Invalid last name."

        # Email validation
        if not email_REGEX.match(postData['email']):
            errors['email'] = "Please use a valid email."

        # Validating if the registered email is unique
        email_duplicate = User.objects.filter(email=postData['email'])
        if email_duplicate:  # Non-EMPTY LIST
            errors['email'] = "Email already in use."

        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters."

        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Password and Password confirmation Should Match."

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    messages = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)

    liker_user = models.ManyToManyField(User, related_name='liked_messages')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    message = models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Like(models.Model):
#     num_of_likes = models.IntegerField()
#     user = models.ForeignKey(User, related_name='user_likes',on_delete=models.CASCADE)
#     message = models.ForeignKey(Message, related_name="liked_comments", on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
