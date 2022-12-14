from django.urls import path
from todolist.views import create_task, show_todolist

from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import finish_task
from todolist.views import delete_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('finish-task/<int:pk>', finish_task, name='finish_task'),
    path('delete-task/<int:pk>', delete_task, name='delete_task'),
]