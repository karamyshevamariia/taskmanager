from django.shortcuts import render, redirect
from django.http import HttpResponse

from mainpage.forms import TaskForm
from mainpage.models import Task


def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'mainpage/index.html',{'title':'Главная страница сайта', 'tasks':tasks })

def about(request):
    return render(request, 'mainpage/about.html')


def create(request):
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            raise ValueError('Форма была не верная')
    form = TaskForm()
    context = {
        'form':form
    }
    return render(request, 'mainpage/create.html', context)