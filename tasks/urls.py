from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_index, name="task_index"),
    path("<str:category>/", views.task_detail, name="task_detail"),
    path("<str:category>/done/<int:pk>", views.make_task_done, name="make_task_done"),
    path("<str:category>/delete/<int:pk>", views.delete_task, name="delete_task"),
]