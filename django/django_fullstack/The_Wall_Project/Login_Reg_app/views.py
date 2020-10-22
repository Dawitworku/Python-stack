from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt
from datetime import datetime, date, timezone


# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        # print(request.POST)

        errors = User.objects.validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

            this_user = User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                password = hashed_pw,
            )
            request.session['user_id'] = this_user.id
            return redirect('/')
    return redirect('/')

def login(request):
    if request.method == "POST":
        this_user = User.objects.filter(email=request.POST['email'])
        if len(this_user) == 1:  # Filter return a list on objects that exist in our DB
            this_user = this_user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), this_user.password.encode()):
                #storing the user identity in our sessions here
                request.session['user_id'] = this_user.id
                return redirect('/wall')
            
        messages.error(request, "Email or Password not found")

    return redirect('/')


def logout(request):
    request.session.flush()
    return redirect('/')


def wall_page(request):

    if 'user_id' not in request.session:  # making sure only logged in users are using the app
        messages.error(request, "You need to Login on create an account!")
        return redirect('/')
    else:
        context = {
            'user' : User.objects.get(id=request.session['user_id']),

            'most_recent_message' : Message.objects.all().order_by('-created_at'),
        }
        #messages.success(request, "Successfully Logged in!")
    return render(request, 'wall.html', context)


def post_message(request):
    if 'user_id' not in request.session:
        messages.error(request, 'You need to Login on create an account!')
        return redirect('/')
    if request.method == "POST":
        print(request.POST)
        print(request.session['user_id'])
        Message.objects.create(
            messages= request.POST['post'],
            user= User.objects.get(id = request.session['user_id'])
        )
        return redirect('/wall')

def post_comment(request, mess_id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to Log in or create an account!")
        return redirect('/')
    if request.method =="POST":
        message_with_id = Message.objects.filter(id = mess_id)#returns a Message Object
        if len(message_with_id) > 0:
            message_object = message_with_id[0]
            print(request.POST)
            print(message_object)
            
            Comment.objects.create(
                comment= request.POST['comment'],
                message= Message.objects.get(id=message_object.id),
                user= User.objects.get(id = request.session['user_id'])
            )
    return redirect('/wall')
 
def delete_message(request, id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to Login on create an account!")
        return redirect('/')
    if request.method == 'POST':
        validated_mess_object = Message.objects.filter(id =id) #returns a Message Object
        if len(validated_mess_object) > 0:
            message_object = validated_mess_object[0]
            print(message_object.id)
            
    #validating if the message to be deleted has been created within thr last 30 minutes.
            mess_created_at_time = message_object.created_at
            now = datetime.now(timezone.utc)
            delete_window = now - mess_created_at_time
            
            if message_object.user.id == request.session['user_id'] and delete_window.seconds < 1800:
                message_to_delete = Message.objects.get(id= message_object.id)
                message_to_delete.delete()
            else:
                messages.error(request, "Time since posted exceeds 30min. Can't be deleted")
    return redirect('/wall')

def delete_comment(request, id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to Login on create an account!")
        return redirect('/')

    if request.method == "POST":
        validated_comment_object = Comment.objects.filter(id= id) #returns a Comment Object
        if len(validated_comment_object) > 0:
            comment_object = validated_comment_object[0]
            print(comment_object.id)

            if comment_object.user.id == request.session['user_id']:
                comment_to_be_deleted = Comment.objects.get(id=comment_object.id)
                comment_to_be_deleted.delete()
    return redirect('/wall')


def messages_likes(request, id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to Login on create an account!")
        return redirect('/')
    if request.method == "POST":
        validated_mess_object = Message.objects.filter(id= id)
        if len(validated_mess_object) > 0:
            mess_object = validated_mess_object[0]
            print(mess_object.id)

            liked_message = Message.objects.get(id=mess_object.id)
            user_liking = User.objects.get(id= request.session['user_id'])
            #creating a like in our DB

            liked_message.liker_user.add(user_liking)
            
    return redirect('/wall')


def messages_unlike(request, id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to Login on create an account!")
        return redirect('/')
    if request.method == "POST":
        validated_mess_object = Message.objects.filter(id= id)
        if len(validated_mess_object) > 0:
            mess_object = validated_mess_object[0]
            print(mess_object.id)

            unliked_message = Message.objects.get(id=mess_object.id)
            user_unliking = User.objects.get(id= request.session['user_id'])
            #creating a like in our DB

            unliked_message.liker_user.remove(user_unliking)
            
    return redirect('/wall')