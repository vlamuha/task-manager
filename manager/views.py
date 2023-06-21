from django.shortcuts import render

from manager.models import Worker, Task


def index(request):
    num_workers = Worker.objects.count()
    num_tasks = Task.objects.count()

    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks
    }

    return render(request, "manager/index.html", context=context)
