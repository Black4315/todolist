from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView,FormView
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django import forms


# Create your views here.
class Login(LoginView):
      template_name = 'pages/login.html'
      fields = '__all__'
      redirect_authenticated_user =True
      def get_success_url(self):
            return reverse_lazy('tasks')



class Register(FormView):
      form_class= UserCreationForm
      template_name = 'pages/register.html'
      redirect_authenticated_user =True
      success_url = reverse_lazy('tasks')
      def form_valid(self, form):
          user = form.save()
          if user is not None :
             login(self.request, user)
          return super().form_valid(form)
      def get(self,*args):
            if self.request.user.is_authenticated:
                  return redirect('tasks')
            return super().get(*args)
      

      
class TasksList(LoginRequiredMixin,ListView):
      model = Task
      template_name = 'pages/index.html'
      context_object_name = 'tasks'
      def get_context_data(self, **kwargs) :
            context = super().get_context_data(**kwargs)
            context['tasks'] = context['tasks'].filter(user = self.request.user)
            context['count'] = context['tasks'].filter(comp = False).count()
            search =  self.request.GET.get('search_area') or ''
            if search is not None:
                  context['tasks'] = context['tasks'].filter(title__startswith = search)

            context['search'] = search
            return context
      

class TaskItem(LoginRequiredMixin,DetailView):
      model = Task
      template_name = 'pages/task.html'
      context_object_name = 'task'

class CreateTask(LoginRequiredMixin,CreateView):
      model = Task
      fields = ['title','desc','comp']
      context_object_name = 'form'
      template_name = 'pages/create-task.html'
      success_url = reverse_lazy('tasks')
      def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)

class EditTask(LoginRequiredMixin,UpdateView):
      model = Task
      fields = ['title','desc','comp']
      context_object_name = 'form'
      template_name = 'pages/edit-task.html'
      success_url = reverse_lazy('tasks')
      def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)

class DeleteTask(LoginRequiredMixin,DeleteView):
      model = Task
      template_name = 'pages/delete-task.html'
      success_url = reverse_lazy('tasks')