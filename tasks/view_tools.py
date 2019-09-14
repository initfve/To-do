from datetime import datetime
from .models import Task
import calendar

my_date = datetime.today()
hour = my_date.hour


def get_formatted_date():
    return calendar.day_name[my_date.weekday()] + ", " + str(my_date.day) + " " + calendar.month_name[
        my_date.month]  # pattern example: Wednesday, 4 September


def get_greeting():
    if 5 < hour < 12:
        welcome = "Good morning"
    elif 12 < hour < 18:
        welcome = "Good afternoon"
    else:
        welcome = "Good evening"
    return welcome


def get_detail_category(request, category):
    tasks = Task.objects.filter(done=False).filter(account__username=request.user.get_username()).all()
    done_tasks = Task.objects.filter(done=True).filter(account__username=request.user.get_username()).all()
    number_of_tasks = Task.objects.filter(done=False).filter(account__username=request.user.get_username()).all()

    if category != "All Schedule":
        tasks = tasks.filter(category__title=category).all()
        done_tasks = done_tasks.filter(category__title=category).all()
        number_of_tasks = number_of_tasks.filter(category__title=category).all()

    context = {
        "tasks": tasks,
        "done_tasks": done_tasks,
        "number_of_tasks": number_of_tasks.count(),
        "category": category,
        "date": get_formatted_date(),
        "greeting": get_greeting(),
        "username": request.user.get_username(),
    }
    return context
