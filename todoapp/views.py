from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Task
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')

def home(request):
    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/')

    context = {'tasks':tasks, 'form':form}

    return render(request, 'todoapp/home.html', context)



@login_required(login_url='login')

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}
    return render(request, 'todoapp/update_task.html', context)



@login_required(login_url='login')

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'todoapp/delete.html', context)


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    else:

        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
        
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        
        context = {'form':form}

        return render(request, 'todoapp/register.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
        
        context = {}

        return render(request, 'todoapp/login.html', context)
    



def logoutUser(request):
    logout(request)

    return redirect('login')