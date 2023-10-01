from django.shortcuts import render
from django.views import generic

from manager.models import Task, Worker, Position, TaskType


def index(request):
    return render(request, "manager/index.html")


class TaskListView(generic.ListView):
    model = Task
    template_name = "manager/task_list.html"
    paginate_by = 5


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "manager/task_detail.html"


class WorkerListView(generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = "manager/worker_list.html"
    paginate_by = 5


class WorkerDetailView(generic.DetailView):
    model = Worker
    template_name = "manager/worker_detail.html"


class PositionListView(generic.ListView):
    model = Position
    template_name = "manager/position_list.html"
    paginate_by = 5


class PositionDetailView(generic.DetailView):
    model = Position
    template_name = "manager/position_detail.html"


class TaskTypeListView(generic.ListView):
    model = TaskType
    template_name = "manager/task_type_list.html"
    paginate_by = 5


class TaskTypeDetailView(generic.DetailView):
    model = TaskType
    template_name = "manager/task_type_detail.html"
