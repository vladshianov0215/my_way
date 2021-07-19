from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm

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

def create(request):
    error = ''
    if request.method == 'POST':#when user add task and put btn
        form  = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'from is not correct'


    form = TaskForm()
    context = {
        'form':form,
        'error':error
    }
    return render(request, 'main/create.html',context)
    
 