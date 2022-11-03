
from django.urls import path
from . views import (
    Index,
    DeleteView, 
    todoappupdate,
    RegisterPage,
    CustomLoginView)
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('', Index.as_view(), name='index'),
    path('todo-delete/<int:pk>', DeleteView.as_view(), name="todo-delete"),
    path('todo-update/<int:pk>/', todoappupdate, name="todo-update"),
    path('register/',RegisterPage.as_view(), name='register'),
    path('user-login/',CustomLoginView.as_view(), name='user-login'),
    path('user-logout/',LogoutView.as_view(), name='user-logout'),
    ]