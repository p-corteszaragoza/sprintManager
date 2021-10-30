from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Sprint
from django.urls import reverse_lazy

class SprintViewSet(LoginRequiredMixin, DetailView):
    model = Sprint
    context_object_name = 'sprints'
    fields = '__all__'
    template_name = "sprint/sprint.html"
    success_url = reverse_lazy('sprints')

    search_fields = ('name',)
    ordering_fields = ('end', 'name',)


class SprintListView(ListView):
    model = Sprint
    context_object_name = 'sprints'
    template_name = "sprint/sprint_list.html"

class SprintDeleteView(LoginRequiredMixin, DeleteView):
    model = Sprint
    context_object_name = 'sprints'
    success_url = reverse_lazy('sprints')
    template_name = "sprint/sprint_delete.html"

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)

class SprintDetail(LoginRequiredMixin, DetailView):
    model = Sprint
    context_object_name = 'sprints'
    template_name = 'sprint/sprint_detail.html'

class SprintCreate(LoginRequiredMixin, CreateView):
    model = Sprint
    template_name = "sprint/sprint_form.html"
    fields = '__all__'
    success_url = reverse_lazy('sprints')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SprintUpdate(LoginRequiredMixin, UpdateView):
    model = Sprint
    fields = '__all__'
    template_name = "sprint/sprint_update.html"
    success_url = reverse_lazy('sprints')
