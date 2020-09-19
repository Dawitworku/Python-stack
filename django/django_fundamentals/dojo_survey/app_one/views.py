from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request,'index.html')

def submission(request):
    if request.method == "POST":
        # context = {
        #     "name" : request.POST['name'],
        #     "location" : request.POST['location'],
        #     "language" : request.POST['language'],
        #     "comment" : request.POST['comment'],
        # }
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
      
        print("This is post**********************")
        return redirect('/result')
    else:
        return redirect('/')
    #     return render(request, 'results.html', context)
    # return render(request, 'results.html')

def results(request):
    return render(request, 'results.html')
