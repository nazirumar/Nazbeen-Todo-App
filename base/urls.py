
from django.urls import path
from . views import Index, todoAppDelete, TodoAppUpdate, TodoAppDetail

urlpatterns =[
    path('', Index.as_view()),
    path('todo-delete/<int:pk>', todoAppDelete, name="todo-delete"),
    path('todo-update/<int:pk>/', TodoAppUpdate.as_view(), name="todo-update"),
    path('todo-todo-detail/<int:pk>/', TodoAppDetail.as_view(), name="todo-detail")
    ]