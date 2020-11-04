from django.shortcuts import render, redirect
from .models import User

# Create your views here.


def index(request):
    context = {
        'all_users': User.objects.all(),
    }
    return render(request, 'app_one/index.html', context)


def create(request):
    if request.method == 'POST':
        User.objects.create(name=request.POST['user_name'])
        return redirect('/two')
    return redirect('/one')


def create_ajax(request):
    if request.method == 'POST':

        User.objects.create(name = request.POST['user_name'])
        context = {
            'all_users': User.objects.all(),
        }
    return render(request, 'app_one/table_snippet.html', context)

