from django.shortcuts import render, redirect
from .models import Task

# Create your views here.


def index(request, id=None):
    if request.method == "POST":
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date','')
        task = Task(name=name, priority=priority, date=date)
        task.save()
        return redirect('/')

    task_list = Task.objects.all()
    return render(request,'myapp/index.html', {'task_list': task_list} )

def delete(request, id):
    task = Task.objects.get(id=id)
    print(request.method)
    # print(request.action)
    # if request.method == 'POST':
    task.delete()
    return redirect('/')
    # return render(request, 'myapp/delete.html', {'task': task})