from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskList, Task
from .forms import TaskForms
from django.urls import reverse_lazy
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required(login_url='/landing/')
def taskList(request):
    task_list = TaskList.objects.filter(user=request.user)
    tasks = Task.objects.filter(task_list__user=request.user).select_related('task_list')

    group_task = {}

    for task_list in TaskList.objects.filter(user=request.user):
        task_for_list = tasks.filter(task_list=task_list)
        group_task[task_list] = task_for_list

    context = {
        'group_task': group_task,
        'user': request.user,
    }

    messages.get_messages(request).used = True  # Mark all messages as "read"

    return render(request, 'Task/index.html', context)

@login_required
def add_task_list(request):
    messages.get_messages(request).used = True  # Mark all messages as "read"
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            names = data.get("name", "").strip()

            if not names:
                return JsonResponse({'success': False, 'error': 'Task list name cannot be empty'})

            task_list = TaskList.objects.create(user=request.user, name=names)

            return JsonResponse({'success': True, 'task_list_id': task_list.id, 'name': task_list.name})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON format'})
    return JsonResponse({'success': False, 'error': 'invalid request'})

@login_required
def delete_task_list(request):
    messages.get_messages(request).used = True  # Mark all messages as "read"
    if request.method == 'POST':
        data = json.loads(request.body)
        task_list_id = data.get('tasklist_id')
        print(task_list_id)
        if task_list_id:
            try:
                task_list = TaskList.objects.get(id=task_list_id, user=request.user)
                task_list.delete()
                return JsonResponse({'success': True})
            except TaskList.DoesNotExist:
                return JsonResponse({'success': False, "error": 'Task List not found'})
        return JsonResponse({'success': False, 'error': 'Tasklist ID missing'})
    return JsonResponse({'success': False, 'error': 'invalid request'})

@login_required
def create_task(request):
    messages.get_messages(request).used = True  # Mark all messages as "read"
    tasklist_id = request.GET.get('tasklist_id')
    tasklist = get_object_or_404(TaskList, id=tasklist_id, user=request.user)

    if request.method == 'POST':
        form = TaskForms(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_list = tasklist
            task.save()
            return redirect(reverse_lazy('task_list'))
    else:
        form = TaskForms()

    context = {
        'form': form,
        'task_list': tasklist
    }

    return render(request, 'Task/create_task.html', context)

@login_required
def edit_task(request, taskId):
    messages.get_messages(request).used = True  # Mark all messages as "read"
    task = get_object_or_404(Task, id=taskId)
    if request.method == 'POST':
        form = TaskForms(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('task_list'))
    else:
        form = TaskForms(instance=task)

    context = {
        'form': form,
        'task': task
    }

    return render(request, 'Task/edit_task.html', context)

@login_required
def delete_task(request, task_id):
    messages.get_messages(request).used = True  # Mark all messages as "read"
    if request.method == 'POST':
        try:
            task = get_object_or_404(Task, id=task_id)
            task.delete()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status':'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@login_required
def update_task(request, task_id):
    messages.get_messages(request).used = True  # Mark all messages as "read"
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_status = data.get('status')

            task = Task.objects.get(id=task_id)
            task.status = new_status
            task.save()

            return JsonResponse({ 'status': 'success', 'message': 'Task status update successfully' })
        except Task.DoesNotExist:
            return JsonResponse({ 'status': 'error', 'message': 'Task not found' }, status=404)
        except Exception as e:
            return JsonResponse({ 'status': 'error', 'message': str(e) }, status=500)
    return JsonResponse({ 'status': 'error', 'message': 'invalid request method'}, status=400)

@login_required
def task_detail_json(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    from datetime import date
    today = date.today()
    days_left = None

    if task.deadline:
        delta = (task.deadline - today).days
        if delta > 0:
            days_left = f"{delta} days left"
        elif delta == 0:
            days_left = "Today"
        else:
            days_left = "Overdue"

    return JsonResponse({
        'title': task.title,
        'description': task.description,
        'deadline': task.deadline.strftime("%A, %d-%b-%Y") if task.deadline else "No deadline",
        'status': task.status,
        'days_left': days_left
    })

@login_required
def update_tasklist(request):
    if (request.method == 'POST'):
        try:
            data = json.loads(request.body)
            tasklist_id = data.get('id')
            name = data.get('name')

            if tasklist_id and name:
                try:
                    tasklist = TaskList.objects.get(id=tasklist_id)
                    tasklist.name = name
                    tasklist.save()
                    return JsonResponse({'success':True})
                except TaskList.DoesNotExist:
                    return JsonResponse({'success':False, 'error':'TaskList not found'})
            else:
                return JsonResponse({'success':False, 'error':'Missing data'})
        except json.JSONDecodeError:
            return JsonResponse({'success':False, 'error':'invalid JSON'})
    return JsonResponse({'success':False,'error':'invalid request'})
