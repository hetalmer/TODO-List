from asyncio import Task
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Tasks
from .taskform import TasksForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
    form = TasksForm()
    form_data = Tasks.objects.all()
    return render(request,'task/index.html',{
        'form':form,
        'formdata':form_data
    })

def edit(request,slug):
    inst = Tasks.objects.get(id=slug)
    form = TasksForm(instance=inst)
    if request.method == 'POST':
        form = TasksForm(request.POST,instance=inst)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request,'task/edit.html',{
        'form':form
    })

def delete(request,slug):
    Tasks.objects.get(id=slug).delete()
    return redirect('/')