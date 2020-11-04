from django.shortcuts import render, redirect
from app_one.models import User

# Create your views here.
def index(request):
    context= {
        'all_users' : User.objects.all()
    }
    return render(request,'app_two/index.html', context)
