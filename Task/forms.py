from django import forms
from .models import Task, TaskList

class TaskForms(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'deadline', 'priority', 'description']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'priority': forms.Select(attrs={'class':'form-control'}),
        }

class TaskListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['name']
        