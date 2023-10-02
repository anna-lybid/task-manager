from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import WorkerSearchForm, PositionsSearchForm, TaskSearchOrderForm, TaskTypeSearchForm
from manager.models import Task, Worker, Position, TaskType


def index(request):
    return render(request, "manager/index.html")


def learn_more(request):
    return render(request, "includes/learn_more.html")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "manager/task_list.html"
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        form = TaskSearchOrderForm(self.request.GET)
        context["search_form"] = form

        sort_by = self.request.GET.getlist("sort_by")
        context["sort_by"] = sort_by

        active_only = self.request.GET.get("active_only", False)
        context["active_only"] = active_only

        return context

    def get_queryset(self):
        queryset = super(TaskListView, self).get_queryset()
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)

        sort_by = self.request.GET.getlist("sort_by")

        if 'deadline' in sort_by:
            queryset = queryset.order_by('deadline')
        elif 'priority' in sort_by:
            queryset = queryset.order_by('priority')

        active_only = self.request.GET.get("active_only", False)
        if active_only:
            queryset = queryset.filter(is_completed=False)

        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "manager/task_detail.html"


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
    template_name = "manager/worker_list.html"
    paginate_by = 9

    def get_queryset(self):
        queryset = super(WorkerListView, self).get_queryset()
        query = self.request.GET.get("query")

        if query:
            queryset = queryset.filter(
                Q(username__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            )

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        context["search_form"] = WorkerSearchForm(
            initial={
                "query": self.request.GET.get("query", ""),
            }
        )
        return context


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    template_name = "manager/worker_detail.html"


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
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PositionListView, self).get_context_data(**kwargs)
        context["search_form"] = PositionsSearchForm(
            initial={
                "name": self.request.GET.get("name", ""),
            }
        )
        return context

    def get_queryset(self):
        queryset = super(PositionListView, self).get_queryset()
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position
    template_name = "manager/position_detail.html"


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
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskTypeListView, self).get_context_data(**kwargs)
        context["search_form"] = TaskTypeSearchForm(
            initial={
                "name": self.request.GET.get("name", ""),
            }
        )
        return context

    def get_queryset(self):
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