from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from manager.models import Worker, Position, Task, TaskType


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = ("task_type", "priority")
    search_fields = ("name",)
    list_display = (
        "name",
        "description",
        "deadline_date",
        "is_completed",
        "priority",
        "task_type",
    )


admin.site.register(TaskType)

admin.site.register(Position)
