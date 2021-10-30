from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from taskManager.models import Task
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class UserSignUpListView(FormView):
    template_name = 'user_sign_up.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserSignUpListView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(UserSignUpListView, self).get(*args, **kwargs)



class UserLoginListView(LoginView):
    template_name = 'user_login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')