from django.urls import path

from tasks.views import (
    index,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskDeleteView,
    WorkerListView,
    WorkerDetailView,
    WorkerUpdateView,
    PositionListView,
    PositionDetailView,
    PositionDeleteView,
    TaskTypeListView,
    TaskTypeDetailView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
    TaskUpdateView,
    WorkerCreateView,
    PositionCreateView,
    TaskTypeCreateView,
    WorkerDeleteView,
    toggle_assign_to_task,
)


urlpatterns = [
    path("", index, name="index"),
    path("task_list/", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "task/<int:pk>/toggle-assign/",
        toggle_assign_to_task,
        name="toggle-task-assign",
    ),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("worker/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
    path("positions/", PositionListView.as_view(), name="positions-list"),
    path("positions/<int:pk>/", PositionDetailView.as_view(), name="positions-detail"),
    path("positions/create/", PositionCreateView.as_view(), name="position-create"),
    path(
        "positions/<int:pk>/delete",
        PositionDeleteView.as_view(),
        name="positions-delete",
    ),
    path("task_types/", TaskTypeListView.as_view(), name="task-types"),
    path("task_types/<int:pk>/", TaskTypeDetailView.as_view(), name="task-type-detail"),
    path("task_types/create", TaskTypeCreateView.as_view(), name="task-type-create"),
    path(
        "task_types/<int:pk>/update",
        TaskTypeUpdateView.as_view(),
        name="task-type-update",
    ),
    path(
        "task_types/<int:pk>/delete",
        TaskTypeDeleteView.as_view(),
        name="task-type-delete",
    ),
]

app_name = "tasks"
