from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def random_word(request):
    # context = {
    #     'counter' : 0,
    #     'ran_word' : get_random_string(length=14),
    # }
# validating here. When we the user go to this page at first, you want the counter to
#start of at "0". Then after, eachtime the user refresh the page or hit the generate button, you would want to increment the number by one to keep count of each attempt.
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1

    request.session['ran_word'] = get_random_string(length=14)
    return render(request,'index.html')

def landing_page(request):
    return redirect("/random_word")
    
# function that resets the counter and redirect back to localhost/random_word.
def reset(request):
    if 'counter' in request.session :
        # request.session['counter'] = 0
        request.session.flush()

    return redirect('/random_word')
    