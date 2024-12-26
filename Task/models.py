from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class TaskList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Task(models.Model):

    PRIORITY_LEVELS = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
        (4, 'Critical')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('To Do','To Do'), ('In Progress', 'In Progress'), ('Completed','Completed')], default='To Do')
    deadline = models.DateField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_LEVELS, default=1)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='task', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['deadline']