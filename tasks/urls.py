from django.urls import path
from .views import (
    index,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskDeleteView,
    WorkerListView,
    WorkerDetailView,
    WorkerUpdateView,
    PositionListView,
)


urlpatterns = [
    path("", index, name="index"),
    path("task_list/", TaskListView.as_view(), name="task_list"),
    path("task_list/", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view, name="task-delete"),
    path("worker_list/", WorkerListView.as_view(), name="worker-list"),
    path("worker/<int:pk>/detail/", WorkerDetailView.as_view(), name="worker-detail"),
    path("worker/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("positions/", PositionListView.as_view(), name="positions-list"),
]

app_name = "tasks"
