from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import  CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = "task/task_list.html"


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/task_detail.html'

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')
    template_name = "task/task_delete.html"

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "task/task_form.html"
    fields = '__all__'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    template_name = "task/task_update.html"
    success_url = reverse_lazy('tasks')
