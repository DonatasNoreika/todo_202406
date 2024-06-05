from django.shortcuts import render
from django.views import generic
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks.html"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    context_object_name = "task"
    template_name = "task.html"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = ['title', 'summary']
    template_name = "task_form.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
