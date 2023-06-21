from django.urls import path
from .views import (
    index,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
)


urlpatterns = [
    path("", index, name="index"),
    path("task_list/", TaskListView.as_view(), name="task_list"),
    path("task_list/", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
]

app_name = "manager"
