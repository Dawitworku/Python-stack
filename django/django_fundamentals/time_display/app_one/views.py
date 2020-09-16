from django.shortcuts import render
from time import gmtime, strftime
from datetime import datetime
from pytz import timezone
# Create your views here.

def index(request):
    context = {
        # "time": strftime("%a, %b %d %Y %H:%M:%S", gmtime())
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%H:%M %p", gmtime())
    }
    return render(request, 'index.html', context)
