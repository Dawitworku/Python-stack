from django.db import models

# Create your models here.


class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['name']) < 5:
            errors['name'] = "Course name must be at least 5 characters"
        if len(postData['description']) < 15:
            errors['description'] = "Course description must be at least 15 characters"
        return errors

class CommentManager(models.Manager):
    def comment_validator(self, postData):
        errors = {}

        if len(postData['comment']) < 5:
            errors['comment'] = "Comments should be at least 5 characters"
        return errors


class Description(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description, related_name='course',on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Comment(models.Model):
    course_comment = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()