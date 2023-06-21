from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from manager.models import Worker, Position, Task, TaskType


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = ("task_type",)
    search_fields = ("name",)


admin.site.register(TaskType)

admin.site.register(Position)
