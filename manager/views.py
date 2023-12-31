from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.db.models.query import QuerySet

from typing import Any, Dict

from manager.forms import (
    WorkerSearchForm,
    PositionsSearchForm,
    TaskTypeSearchForm,
    TaskSearchForm,
    TaskOrderForm,
)
from manager.models import Task, Worker, Position, TaskType


def index(request) -> HttpResponse:
    return render(request, "manager/index.html")


def learn_more(request)  -> HttpResponse:
    return render(request, "includes/learn_more.html")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs) -> Dict[str, Any]:
        context = super(TaskListView, self).get_context_data(**kwargs)
        search_form = TaskSearchForm(self.request.GET)
        order_form = TaskOrderForm(self.request.GET)

        context["search_form"] = search_form
        context["order_form"] = order_form

        return context

    def get_queryset(self) -> "QuerySet[Task]":
        queryset = super(TaskListView, self).get_queryset()
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)

        sort_by = self.request.GET.getlist("sort_by")

        if "deadline" in sort_by:
            queryset = queryset.order_by("deadline")
        elif "priority" in sort_by:
            queryset = queryset.order_by("priority")

        active_only = self.request.GET.get("active_only", False)
        if active_only:
            queryset = queryset.filter(is_completed=False)

        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("manager:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("manager:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:task-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    paginate_by = 7

    def get_queryset(self) -> "QuerySet[Worker]":
        queryset = super(WorkerListView, self).get_queryset()
        query = self.request.GET.get("query")

        if query:
            queryset = queryset.filter(
                Q(username__icontains=query)
                | Q(first_name__icontains=query)
                | Q(last_name__icontains=query)
            )

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs) -> Dict[str, Any]:
        context = super(WorkerListView, self).get_context_data(**kwargs)
        context["search_form"] = WorkerSearchForm(
            initial={
                "query": self.request.GET.get("query", ""),
            }
        )
        return context


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    fields = "__all__"
    success_url = reverse_lazy("manager:worker-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    fields = "__all__"
    success_url = reverse_lazy("manager:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("manager:worker-list")


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    template_name = "manager/position_list.html"
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs) -> Dict[str, Any]:
        context = super(PositionListView, self).get_context_data(**kwargs)
        context["search_form"] = PositionsSearchForm(
            initial={
                "name": self.request.GET.get("name", ""),
            }
        )
        return context

    def get_queryset(self) -> "QuerySet[Position]":
        queryset = super(PositionListView, self).get_queryset()
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("manager:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("manager:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("manager:position-list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "manager/task_type_list.html"
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs) -> Dict[str, Any]:
        context = super(TaskTypeListView, self).get_context_data(**kwargs)
        context["search_form"] = TaskTypeSearchForm(
            initial={
                "name": self.request.GET.get("name", ""),
            }
        )
        return context

    def get_queryset(self) -> "QuerySet[TaskType]":
        queryset = super(TaskTypeListView, self).get_queryset()
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    template_name = "manager/task_type_detail.html"


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("manager:task-type-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("manager:task-type-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("manager:task-type-list")
