from django.shortcuts import render, redirect, HttpResponse
from .models import Show

# Create your views here.

def all_shows(request):
    context = {
        'all_shows' : Show.objects.all(),
    }
    return render(request, 'all_shows.html', context)

def new_show(request):
    context = {

    }
    return render(request, 'add_show.html')

def create_show(request):
    if request.method == "POST":
        print(request.POST)  ###### ##############To be deleted
        # Create the show in the DB
        this_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date= request.POST['release_date'], description= request.POST['description'])
        # Grabbing the ID of the show after creating to redirect to the shows page right away.
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
