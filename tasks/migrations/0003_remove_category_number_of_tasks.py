# Generated by Django 2.2.5 on 2019-09-06 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='number_of_tasks',
        ),
    ]
