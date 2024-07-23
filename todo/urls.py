from django.urls import path
from todo import views

urlpatterns = [
    path("todo_list/", views.todo_list, name="todo_list"),
    path("todo_list/<int:pk>", views.todo_detail, name="todo_detail"),
]