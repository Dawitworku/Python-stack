from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        errors = User.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            hashed_pw = bcrypt.hashpw(
                request.POST['password'].encode(), bcrypt.gensalt()).decode()

            user = User.objects.create(
                name=request.POST['user_name'],
                email=request.POST['email'],
                password=hashed_pw
            )
            # storing user id inside of sessions upon the creation of a user.
            request.session['user_id'] = user.id
            return redirect('/main_page')  # the main page of the application

    return redirect('/')


def login(request):
    # Validating users email
    # filter always return a list [] so we need to get the user from the list
    user = User.objects.filter(email=request.POST['email'])
    if len(user) > 0:
        user = user[0]  # new value of our varable user.
        # validating password
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            # storing the users_id inside our sessions
            # why do i need to to this again here
            request.session['user_id'] = user.id
            return redirect('/main_page')
    else:
        messages.error(request, "Email or password is incorrect")
        return redirect('/')


def main_page(request):
    if 'user_id' not in request.session:  # making sure only logged in users are using the app
        messages.error(request, "You need to register or log in!")
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=request.session['user_id']),
            'all_koalas': Koala.objects.all()
        }
    return render(request, 'main_page.html', context)


def create_koala(request):
    if request.method == "POST":
        errors = Koala.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                # return redirect('/main_page')
        else:
            koala = Koala.objects.create(
                name=request.POST['koala_name'],
                talent=request.POST['talent'],
                # an object of the user. Not just the key from the session which is just an id.
                user=User.objects.get(id=request.session['user_id'])
            )
    return redirect('/main_page')


def logout(request):
    request.session.flush()
    return redirect('/')


def profile(request):
    if 'user_id' not in request.session:
        message.error(request, "You need to register or log in!")
        return redirect('/')

    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'profile.html', context)


# Why can't i still use sessions instad of using ID and pass it through the url
def show_koala(request, id):
    if 'user_id' not in request.session:
        message.error(request, "You need to register or log in!")
        return redirect('/')
    # Validating to see if the Koala exists in our Database to avoid url manipulation by using the ID
    koala_with_id = Koala.objects.filter(id=id)  
    if len(koala_with_id) > 0:
        context = {
            'koala': Koala.objects.get(id=id) # Grabing the Koala object here
        }
        return render(request, 'one_koala.html', context)

    else:  # extra validation incase user manipulates the url by changing the id
        messages.error(request, "Koala not found")
        return redirect('/user')


def destroy_koala(request, id):
    if 'user_id' not in request.session:
        message.error(request, "You need to register or log in!")
        return redirect('/')

    if request.method == "POST":
        # Validating to see if the Koala exists in our Database to avoid url manipulation by using the ID
        koala_with_id = Koala.objects.filter(id=id)
        if len(koala_with_id) > 0:
            koala = koala_with_id[0]
            #extra validation to avoid user manipulating and deleting a koala by editting the url.
            if (koala.user.id == request.session['user_id']): 
                koala.delete()

    return redirect('/main_page')
