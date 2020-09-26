from django.shortcuts import render, redirect, HttpResponse
import random
from datetime import datetime

# Create your views here.
def index(request):# When you start the game, your ninja should have 0 gold.
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'ninja.html')

def process_money(request):
    if request.method == "POST":
        print(request.POST)

        target = request.POST['building']

        map = { # randint method -randrange(start, stop+1)
            'farm': random.randrange(10,21),
            'cave': random.randrange(5, 11),
            'house': random.randrange(2, 6),
            'casino': random.randrange(-50, 51),
        }
        
        request.session['gold'] = map[target] + request.session['gold']
        time_stamp = datetime.now().strftime("%Y/%m/%d %I:%M %p")
    
        if target == 'farm':
            request.session['activities'].append(f"Earned  {map['farm']} golds from the farm! ({time_stamp})")
        elif target == 'cave':
            request.session['activities'].append(f"Earned  {map['cave']} golds from the cave! ({time_stamp})")
        elif target == 'house':
            request.session['activities'].append(f"Earned  {map['house']} golds from the house! ({time_stamp})")
        elif target == 'casino' and map['casino'] > 0:
            request.session['activities'].append(f"Entered a casino and earned {map['casino']} golds...Nice.. ({time_stamp})")

        elif target == 'casino' and map['casino'] < 0:
            request.session['activities'].append(f"Entered a casino and lost {abs(map['casino'])} golds...Ouch.. ({time_stamp})")
    return redirect("/")

def reset(request):
    if request.method == 'POST':
        request.session.flush()
        return redirect('/')    
