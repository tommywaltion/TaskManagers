# Generated by Django 5.1.3 on 2024-12-23 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0006_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-is_urgent', 'deadline']},
        ),
        migrations.AddField(
            model_name='task',
            name='is_urgent',
            field=models.BooleanField(default=False),
        ),
    ]