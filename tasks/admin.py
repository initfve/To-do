from django.contrib import admin
from .models import Category, Task


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass


class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(Task, TaskAdmin)
admin.site.register(Category, CategoryAdmin)
