from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    path('logout/', LogoutView.as_view(next_page='tasks'), name='logout'),
    path("", TasksList.as_view(), name="tasks"),
    path("task/<int:pk>", TaskItem.as_view(), name="task"),
    path("create-task/", CreateTask.as_view(), name="create-task"),
    path("Edit-task/<int:pk>", EditTask.as_view(), name="edit-task"),
    path("Delete-task/<int:pk>", DeleteTask.as_view(), name="delete-task"),
]
