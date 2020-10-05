from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages  # Importing messages framework here
from .models import Show

# Create your views here.

def all_shows(request):
    context = {
        'all_shows' : Show.objects.all(),
    }
    return render(request, 'all_shows.html', context)

def new_show(request):
    
    return render(request, 'add_show.html')

def create_show(request):
    if request.method == "POST":
        errors = Show.objects.show_validator(request.POST) # passing the post date to the validator
        if len(errors) > 0:  # checking if there is any errors.
            for key,value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
    # VALIDATING IF A TITLE EXISTS
        if Show.objects.filter(title__iexact= request.POST['title']).exists():
            #creating a messsage to be displayed it we enter a title that already exists in the DB
            messages.error(request, "This title already exists")
            return redirect(f'/shows/new')

        else: # if everything is good and no errors -->
            # Create the show in the DB
            this_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date= request.POST['release_date'], description= request.POST['description'])
            # Grabbing the ID of the show after creating to redirect to the shows page right away.
            messages.success(request, "Show successfully created")

            id = this_show.id
            return redirect(f'/shows/{id}')

def show_shows(request, id):
    context = {
        'a_show' : Show.objects.get(id = id)
    }
    this_show = Show.objects.get(id = id)
    print(this_show.release_date) ###########################to be deleted
    return render(request, 'show_shows.html', context)

def edit_show(request, id):
    context = {
        'one_show' : Show.objects.get(id = id)
    }
    return render(request, 'edit_show.html',context)

def update(request, id):
    if request.method == "POST":
        errors = Show.objects.show_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{id}/edit')

        target = Show.objects.get(id = id)
        if request.POST['title'] == target.title: # comparing a title here
            #creating a messsage to be displayed it we enter a title that already exists in the DB
            messages.info(request, "This title already exists")
            return redirect(f'/shows/{id}/edit')
        else:   
        # Grabbing a show to be updated by the ID
            show_to_be_updated = Show.objects.get(id = id)
            show_to_be_updated.title = request.POST['title']
            show_to_be_updated.network = request.POST['network']
            show_to_be_updated.release_date = request.POST['release_date']
            show_to_be_updated.description = request.POST['description']
            show_to_be_updated.save()

    return redirect(f'/shows/{id}')

def destroy(request, id):
    # Grabbing a show to be deleted by the ID
    show_to_delete = Show.objects.get(id= id)
    show_to_delete.delete()
    return redirect('/shows')
