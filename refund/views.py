from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
     'title' : 'Refund'
    }
    return render(request,'refund/index.html', context)
