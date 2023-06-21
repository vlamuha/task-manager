from django.urls import path
from .views import (
    index,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskDeleteView,
    WorkerListView,
)


urlpatterns = [
    path("", index, name="index"),
    path("task_list/", TaskListView.as_view(), name="task_list"),
    path("task_list/", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view, name="task-delete")
    path("worker_list/", WorkerListView.as_view(), name="worker-list"),
]

app_name = "tasks"