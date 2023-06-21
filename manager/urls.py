from django.urls import path
from .views import (
    index,
    TaskListView,
)


urlpatterns = [
    path("", index, name="index"),
    path("task_list/", TaskListView.as_view(), name="task_list"),
]

app_name = "manager"
