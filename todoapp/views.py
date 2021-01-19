from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Todo
from .forms import *


# Create your views here.
def home(request):
    something = Todo.objects.order_by('-date')
    print(something)
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'something': something,'form':form}
    return render(request,'todo/index.html', context)


def UpdateTask(request, pk):
    task = Todo.objects.get(id = pk)
    
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form }

    return render(request,'todo/update_task.html', context)

def deletetask(request, pk):
    print('inside delete func')
    item  = Todo.objects.get(id = pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    
        

    context = {'item' : item }
    return render(request,'todo/delete.html', context)