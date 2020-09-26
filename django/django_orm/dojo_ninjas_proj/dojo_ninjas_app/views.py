from django.shortcuts import render, redirect, HttpResponse
from dojo_ninjas_app.models import *


# Create your views here.
def landing_page(request):
    context = {
        "all_existing_dojos" : Dojos.objects.all(),
    }
    return render(request, 'dojo_ninjas.html', context)


def process_one(request):
    if request.method =="POST":
        if request.POST['action'] == 'Add_dojo':

            name = request.POST['name']
            city = request.POST['city']
            state = request.POST['state']
            Dojos.objects.create(name=name, city=city, state=state)
        return redirect("/")

def process_two(request):
    if request.method == "POST":
        if request.POST['action'] == "Add_ninja":

            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            dojo = request.POST['dojo']

            instance = Dojos.objects.get(name= dojo) # dojo refers to each campus user creates

            print(dojo)  #delete this***
            Ninjas.objects.create(first_name=first_name, last_name=last_name, dojo= instance)
        return redirect("/")

def delete(request, id):
    # if request.method == "POST":

        # target = request.POST['delete']
        # print(target)
        # dojo_to_be_deleted = Dojos.objects.get(name= target)
        #dojo_to_be_deleted.delete()
#OR

    dojo_to_be_deleted = Dojos.objects.get(id = id)
    dojo_to_be_deleted.delete()

    return redirect('/')