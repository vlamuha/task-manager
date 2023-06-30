from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tasks.models import Worker, Position, Task, TaskType


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    list_filter = ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                    )
                },
            ),
        )
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = ("task_type", "priority")
    search_fields = ("name",)
    list_display = (
        "name",
        "description",
        "deadline",
        "is_completed",
        "priority",
        "task_type",
    )


admin.site.register(TaskType)

admin.site.register(Position)
