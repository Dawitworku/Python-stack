from django.shortcuts import render, redirect, HttpResponse
from books_authors_app.models import *
# Create your views here.

def landing_page(request):
    context = {
        'all_books': Book.objects.all(),
    }
    return render(request, 'books.html', context)

def authors(request):
    context = {
        'all_authors': Author.objects.all(),
    }
    return render(request, 'authors.html', context)

def authors_page(request):
    if request.method == "POST":
        if request.POST['action'] == "Add_author":

            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            notes = request.POST['notes']
            
            Author.objects.create(first_name= first_name, last_name= last_name, notes= notes)
    return redirect('/authors')

def books(request):
    if request.method == "POST":
        if request.POST['action'] == "Add_book":

            title = request.POST['title']
            description = request.POST['description']

            Book.objects.create(title= title, desc= description)
        return redirect('/')

def view_book(request, id):## id is book-id
    context = {
        'book' : Book.objects.get(id = id),
        # 'all_authors': Author.objects.all(),
        'authors_not_contributors_for_this_book_filter' : Author.objects.exclude(books= id),
    }
    return render(request, 'from_book.html', context)

def view_author(request, id): # id is authors id
    context = {
        'author' : Author.objects.get(id= id),
        # 'all_books' : Book.objects.all(),
        'books_not_by_this_author_filter' : Book.objects.exclude(authors= id),
    }
    return render(request, 'from_authors.html', context)

def author_form(request, id):
    
    if request.method == "POST":
        author_id = request.POST['author_id']
        print(author_id)

        book = Book.objects.get(id = id)
        author = Author.objects.get(id= author_id)
        author.books.add(book)

    return redirect(f'/books/{id}')

def book_form(request, id):
    if request.method == "POST":

        book_id = request.POST['book_id']
        print(book_id)
        book = Book.objects.get(id = book_id)
        author = Author.objects.get(id = id)
        book.authors.add(author)

    return redirect(f'/authors/{id}')
