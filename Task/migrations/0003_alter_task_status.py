# Generated by Django 5.1.3 on 2024-12-13 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_rename_tasks_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='To Do', max_length=20),
        ),
    ]