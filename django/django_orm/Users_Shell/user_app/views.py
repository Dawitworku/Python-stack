from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def users(request):
    return HttpResponse('Checking')
    