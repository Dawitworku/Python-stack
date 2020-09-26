from django.shortcuts import render, redirect, HttpResponse
from .models import Dragon, Wizard

# Create your views here.
def index(request):
    context = {
        "all_dragons": Dragon.objects.all(), # using key -value relationship here.
        "filter": Wizard.objects.filter(house="Gryffindor"),
    }
    return render(request, 'index.html', context) 