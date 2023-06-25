from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import (
    WorkerCreationForm,
    PositionSearchForm,
    WorkerSearchForm,
    TaskSearchForm,
    TaskForm,
    PositionForm,
)
from tasks.models import Worker, Task, Position, TaskType


def index(request):
    num_workers = Worker.objects.count()
    num_tasks = Task.objects.all()
    num_positions = Position.objects.all()

    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
        "num_positions": num_positions,
    }

    return render(request, "tasks/index.html", context=context)


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "tasks/task_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = TaskSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = Task.objects.all()
        form = TaskSearchForm(self.request.GET)

        if form.is_valid():
            name = form.cleaned_data["name"]
            if name:
                queryset = queryset.filter(name__icontains=name)
        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")
    template_name = "tasks/task_form.html"


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")
    template_name = "tasks/task_form.html"

    def task_update(request, pk):
        task = get_object_or_404(Task, pk=pk)

        if request.method == "POST":
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect("task_detail", pk=task.pk)
        else:
            form = TaskForm(instance=task)

        return render(request, "tasks/task_form.html", {"form": form})


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    template_name = "tasks/worker_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)

        last_name = self.request.GET.get("last_name", "")

        context["search_form"] = WorkerSearchForm(initial={"last_name": last_name})
        return context

    def get_queryset(self):
        queryset = Worker.objects.all()
        form = WorkerSearchForm(self.request.GET)

        if form.is_valid():
            last_name = form.cleaned_data["last_name"]
            if last_name:
                queryset = queryset.filter(last_name__icontains=last_name)
        return queryset


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("tasks:worker-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("tasks:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("tasks:worker-list")


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    template_name = "tasks/positions.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PositionListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = PositionSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = Position.objects.all()
        form = PositionSearchForm(self.request.GET)

        if form.is_valid():
            name = form.cleaned_data["name"]
            if name:
                queryset = queryset.filter(name__icontains=name)
        return queryset


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position
    template_name = "tasks/position_detail.html"


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy("tasks:positions-list")
    template_name = "tasks/position_form.html"


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("tasks:positions-list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "tasks/task_type_list.html"
    paginate_by = 5
    ordering = ["name"]


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    template_name = "tasks/task_type_detail.html"


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("tasks:task-types")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("tasks:task-types")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("tasks:task-types")


class ToggleAssignToTaskView(generic.View):
    @staticmethod
    def post(request, pk):
        worker = Worker.objects.get(id=request.user.id)
        task = Task.objects.get(id=pk)
        if task in worker.tasks.all():
            worker.tasks.remove(task)
        else:
            worker.tasks.add(task)
        return HttpResponseRedirect(
            reverse_lazy("task_manager:task-detail", args=[pk])
        )
