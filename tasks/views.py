from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Category, Task
from .form import TaskForm
from .view_tools import get_formatted_date, get_greeting, get_detail_category


def task_index(request):
    categories = Category.objects.only("title")
    number_of_tasks = []
    for category in categories:
        if category.title == "All Schedule":
            number_of_tasks.append(
                Task.objects.filter(account__username=request.user.get_username()).filter(done=False).count())
        else:
            number_of_tasks.append(
                Task.objects.filter(account__username=request.user.get_username()).filter(done=False)
                    .filter(category__title=category).count())

    categories = zip(categories, number_of_tasks)
    context = {
        "categories": categories,
        "number_of_tasks": number_of_tasks,
        "date": get_formatted_date(),
        "greeting": get_greeting(),
        "username": request.user.get_username(),
        "created_tasks": Task.objects.filter(account__username=request.user.get_username()).filter(done=False).count(),
        "completed_tasks": Task.objects.filter(account__username=request.user.get_username()).filter(done=True).count(),
    }
    return render(request, 'task_index.html', context)


@login_required
def task_detail(request, category):
    c = Category.objects.get(title=category)
    a = request.user
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.content = form.cleaned_data['content']
            task.category = c
            task.account = a
            task.done = False
            task.save()
            form.clean()
        else:
            print(str(form.errors))

    return render(request, 'task_detail.html', get_detail_category(request, category))


@login_required
def make_task_done(request, category, pk):
    task = Task.objects.get(pk=pk)
    task.done = True
    task.save()
    return render(request, 'task_detail.html', get_detail_category(request, category))


@login_required
def delete_task(request, category, pk):
    Task.objects.get(pk=pk).delete()
    return render(request, 'task_detail.html', get_detail_category(request, category))
