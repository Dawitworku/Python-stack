from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
# Create your views here.
def main(request):
    if request.method == 'GET':
        context = {
            'all_courses' : Course.objects.all()  
        }
        return render(request, 'main.html', context)

def create(request):
    if request.method == 'POST':
        errors = Course.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')

        else:    
            desc = Description.objects.create(content= request.POST['description'])
            cours = Course.objects.create(name= request.POST['name'], description= desc)

            return redirect('/')

def destroy(request, id):
    if request.method == 'GET':
        instance = Course.objects.get(id = id)
        context = {
            'this_course' : instance
        }
        return render(request, 'destroy.html', context)

def delete(request, id):
    if request.method == 'POST':

        course_to_be_deleted = Course.objects.get(id = id)
        course_to_be_deleted.delete()
        return redirect('/')

def comment(request, id):
    if request.method == 'GET':
        instance_of_a_course = Course.objects.get(id = id)
        context = {
            'this_course': instance_of_a_course
        }
        return render(request, 'comment.html', context)

def create_comment(request, id):
    if request.method == "POST":
        errors = Comment.objects.comment_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/comment/{id}')
        else:
            this_course = Course.objects.get(id= id)
            comm = Comment.objects.create(course_comment= request.POST['comment'], course= this_course)

        return redirect(f'/comment/{id}')
