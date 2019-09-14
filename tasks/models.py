from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Category(models.Model):
    title = models.CharField(max_length=20)
    icon = models.CharField(max_length=30)
    account = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Task(models.Model):
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    account = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.content



