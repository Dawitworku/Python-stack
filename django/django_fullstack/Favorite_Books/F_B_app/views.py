from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.
def index(request):
    return render(request,'LogReg.html')

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
                return redirect('/books')
            
        messages.error(request, "Email or Password not found")

    return redirect('/')


def logout(request):
    request.session.flush()
    return redirect('/')


def main_page(request):

    if 'user_id' not in request.session:  # making sure only logged in users are using the app
        messages.error(request, "You need to Login on create an account!")
        return redirect('/')
    else:
        context = {
            'user' : User.objects.get(id=request.session['user_id']),
            'all_books' : Book.objects.all(),
        }
        #messages.success(request, "Successfully Logged in!")
    return render(request, 'favBook.html', context)

def add_book(request):
    if 'user_id' not in request.session:  # making sure only logged in users are using the app
        messages.error(request, "You need to Login on create an account!")
        return redirect('/')
    if request.method == "POST":
        errors = Book.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            print(request.POST)
            print(request.session['user_id'])

            this_user = User.objects.get(id= request.session['user_id'])
            
            books_object = Book.objects.create(
                title= request.POST['title'],
                description= request.POST['description'],
                uploaded_by= this_user,
            )
            books_object.users_who_like.add(this_user)
    
    return redirect('/books')

def show_book(request, id):
    if 'user_id' not in request.session:  # making sure only logged in users are using the app
        messages.error(request, "You need to Login on create an account!")
        return redirect('/')
    Book_with_id = Book.objects.filter(id = id)
    if len(Book_with_id) > 0:
        context = {
            'user' : User.objects.get(id=request.session['user_id']),
            'book': Book.objects.get(id=id)
        }
        return render(request, 'add_fav.html', context)
    else:  # extra validation incase user manipulates the url by changing the id
        messages.error(request, "Book not found")
        return redirect('/books')

def edit_book(request, id): # add validations
    if 'user_id' not in request.session:  # making sure only logged in users are using the app
        messages.error(request, "You need to Login on create an account!")
        return redirect('/')
    if request.method =='POST':
        errors = Book.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:       
            book_with_id = Book.objects.filter(id = id)
            if len(book_with_id) > 0:
                book_object = book_with_id[0]
                #print(request.POST)
                this_book = Book.objects.get(id =book_object.id)
                # Validating to prevent the logged in user from editting other peoples post/book *****
                if this_book.uploaded_by.id == request.session['user_id']:
                    this_book.title = request.POST['title']
                    this_book.description = request.POST['description']
                    this_book.save()
    return redirect(f'/books/{id}')

def delete_book(request): # should i pass the id through he url or hidden input lik this?**************************

    if 'user_id' not in request.session:  # making sure only logged in users are using the app
        messages.error(request, "You need to Login on create an account!")
        return redirect('/')
    if request.method == 'POST':
        print(request.POST) 

        book_with_id = Book.objects.filter(id= request.POST['delete_book'] )
        if len(book_with_id) > 0:
            book_object = book_with_id[0]
        
            book_to_be_deleted = Book.objects.get(id= book_object.id)
            # Validating to prevent the logged in user from deleting other peoples book ***** 
            # only users who created the book can delete
            if book_to_be_deleted.uploaded_by.id == request.session['user_id']:
                book_to_be_deleted.delete()
    return redirect('/books')

def unfav_book(request, id):
    if 'user_id' not in request.session:  # making sure only logged in users are using the app
        messages.error(request, "You need to Login on create an account!")
        return redirect('/')
    if request.method == "POST":
        Book_w_id = Book.objects.filter(id = id) #returns a list of bookobjects if it exists
        if len(Book_w_id) > 0:
            book_object = Book_w_id[0]

            un_faved_book = book_object
            user_unfavoriting = User.objects.get(id= request.session['user_id'])

            un_faved_book.users_who_like.remove(user_unfavoriting)
    return redirect(f'/books/{id}')


def add_fav_book(request, id):
    if 'user_id' not in request.session:  # making sure only logged in users are using the app
        messages.error(request, "You need to Login on create an account!")
        return redirect('/')
    if request.method == "POST":
        book_with_id = Book.objects.filter(id =id)
        if len(book_with_id) > 0:
            book_object = book_with_id[0]

            favBook = book_object
            user_adding_book = User.objects.get(id=request.session['user_id'])

            favBook.users_who_like.add(user_adding_book)
    return redirect(f'/books/{id}')