from django.shortcuts import render
from todolist.models import TaskTodolist

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = TaskTodolist.objects.filter(user = request.user)
    #data_todolist = TaskTodolist.objects.all()
    context = {
        'data_todolist': data_todolist,
        'nama': 'Muhammad Raihan',
        'id': '2106654643',
        'username': request.user.username,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        user = request.user
        is_finished = False
        TaskTodolist.objects.create(title=title, description=description, date=date, user=user, is_finished=is_finished)
        return redirect('todolist:show_todolist')
    return render(request,"createTask.html")

# Fungsi yang mengganti status task
def finish_task(request, pk):
    task = TaskTodolist.objects.get(id=pk)
    task.is_finished = True
    task.save()
    return redirect('todolist:show_todolist')

# Fungsi yang menghapus task
def delete_task(request, pk):
    task = TaskTodolist.objects.get(id=pk)
    TaskTodolist.delete(task)
    return redirect('todolist:show_todolist')
