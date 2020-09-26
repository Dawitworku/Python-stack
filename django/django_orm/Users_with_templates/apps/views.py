from django.shortcuts import render, redirect, HttpResponse
from apps.models import User
from django.contrib import messages

# Create your views here.

def index(request):
    context =  {
        "all_users": User.objects.all()
    }
    return render(request, "index.html", context)

def process(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect("/")

    elif request.method == "POST":

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        age = request.POST['age']

        #creating and passing user value to our database
        User.objects.create(first_name=first_name, last_name=last_name, email=email, age=age)
        
    return redirect("/")

