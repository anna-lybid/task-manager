from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from manager.models import Task, Worker, Position, TaskType


@login_required
def index(request):
    return render(request, "manager/index.html")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "manager/task_list.html"
    paginate_by = 5


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "manager/task_detail.html"


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = "manager/worker_list.html"
    paginate_by = 5


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    template_name = "manager/worker_detail.html"


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    template_name = "manager/position_list.html"
    paginate_by = 5


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position
    template_name = "manager/position_detail.html"


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "manager/task_type_list.html"
    paginate_by = 5


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    template_name = "manager/task_type_detail.html"
