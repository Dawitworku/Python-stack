from django.shortcuts import render, redirect, HttpResponse
from .models import *
# Create your views here.

def main(request):
    #show all dogs in DB
    context = {
        'all_dogs' : Dog.objects.all(),
    }
    return render(request, 'orm_lec.html', context)

def create_form(request):
    #show a form to create a dog
    return render(request, 'create.html')

def create_dog(request):
    #create an instance of the dog class
    if request.method == "POST":
        print(request.POST)
        Dog.objects.create(name=request.POST['dog_name'], age = request.POST['dog_age'])
    return redirect('/')

def show_dog(request, id):
    #shoe onr instance of a dog on a template 
    context = {
        'one_dog' : Dog.objects.get(id= id)
    }
    return render(request, 'one_dog.html', context)

def delete_dog(request, id):
    # delete a dof from the DB
    if request.method == "POST":
        dog_to_delete = Dog.objects.get(id=id)
        dog_to_delete.delete()
    return redirect('/')

def edit_dog(request, id):
    # shoe a form to edit a dog
    context = {
        'one_dog' : Dog.objects.get(id= id)
    }
    return render(request, "one_dog_edit.html", context)

def update_dog(request, id):
    if request.method == "POST":
        dog_to_update = Dog.objects.get(id= id)
        dog_to_update.name = request.POST['dog_name']
        dog_to_update.age = request.POST['dog_age']
        dog_to_update.save()
    return redirect(f'/dogs/{id}')
