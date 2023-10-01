from django.shortcuts import render
from django.views import generic

from manager.models import Task, Worker, Position, TaskType


def index(request):
    """View function for the home page of the site."""
    return render(request, "manager/index.html")


class TaskListView(generic.ListView):
    model = Task
    template_name = "manager/task_list.html"
    paginate_by = 10


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "manager/task_detail.html"


class WorkerListView(generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = "manager/worker_list.html"
    paginate_by = 10


class WorkerDetailView(generic.DetailView):
    model = Worker
    template_name = "manager/worker_detail.html"


class PositionListView(generic.ListView):
    model = Position
    template_name = "manager/position_list.html"
    paginate_by = 10


class PositionDetailView(generic.DetailView):
    model = Position
    template_name = "manager/position_detail.html"


class TaskTypeListView(generic.ListView):
    model = TaskType
    template_name = "manager/task_type_list.html"
    paginate_by = 10


class TaskTypeDetailView(generic.DetailView):
    model = TaskType
    template_name = "manager/task_type_detail.html"