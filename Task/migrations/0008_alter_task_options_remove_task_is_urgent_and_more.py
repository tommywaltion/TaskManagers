# Generated by Django 5.1.3 on 2024-12-23 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0007_alter_task_options_task_is_urgent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-priority', 'deadline']},
        ),
        migrations.RemoveField(
            model_name='task',
            name='is_urgent',
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Critical')], default=1),
        ),
    ]
