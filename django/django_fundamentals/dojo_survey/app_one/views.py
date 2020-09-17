from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def submission(request):

    if request.method == "POST":
        context = {
            "name" : request.POST['name'],
            "location" : request.POST['location'],
            "language" : request.POST['language'],
            "comment" : request.POST['comment'],
        }
        #print(request.POST)
        return redirect('/')
    #     return render(request, 'results.html', context)
    # return render(request, 'results.html')

