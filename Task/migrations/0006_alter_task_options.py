# Generated by Django 5.1.3 on 2024-12-16 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0005_remove_task_user_task_task_list'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['status']},
        ),
    ]
