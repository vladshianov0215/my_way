from django.shortcuts import render
from django.http import HttpResponse

from .models import Task


# Create your views here.
def index(request):
    #Task.objects.find()
    #Task.objects.order_by('-id')# 'id' '-id' [:1] only one  'title'
    #Task.objects.all()
    tasks  = Task.objects.order_by('-id')#new news will be upper
    return render(request, 'main/index.html', {'title':'index_list_name', 'tasks':tasks} )

def about(request):
    return render(request, 'main/about.html')
    #return HttpResponse("<h4>About</h4>")
 