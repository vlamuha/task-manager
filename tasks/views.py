from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import TaskForm, WorkerCreationForm, PositionSearchForm
from tasks.models import Worker, Task, Position, TaskType


def index(request):
    num_workers = Worker.objects.count()
    num_tasks = Task.objects.count()
    num_positions = Position.objects.count()

    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
        "num_positions": num_positions,
    }

    return render(request, "tasks/index.html", context=context)


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "tasks/task_list.html"


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    template_name = "tasks/worker_list.html"


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("tasks:worker-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    fields = "__all__"
    success_url = reverse_lazy("tasks:worker-list")


class WorkerDeleteView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    generic.DeleteView
):
    model = Worker
    success_url = reverse_lazy("tasks:worker-list")


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    template_name = "tasks/positions_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PositionListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = PositionSearchForm(
            initial={"name": name}
        )
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


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("tasks:positions_list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("tasks:positions_list")


class PositionDeleteView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    generic.DeleteView
):
    model = Position
    success_url = reverse_lazy("tasks:positions_list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "tasks/task_type_list.html"


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("tasks:task_type_list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("tasks:task_type_list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("tasks:task_type_list")

    @login_required
    def toggle_assign_to_task(request, pk):
        worker = Worker.objects.get(id=request.user.id)
        if (
            Worker.objects.get(id=pk) in worker.tasks.all()
        ):  # probably could check if car exists
            worker.tasks.remove(pk)
        else:
            worker.tasks.add(pk)
        return HttpResponseRedirect(reverse_lazy("task:task-detail", args=[pk]))
