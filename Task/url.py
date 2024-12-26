from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskList, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('edit/<int:taskId>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('add_list/', views.add_task_list, name='add_task_list'),
    path('delete_list/', views.delete_task_list, name='delete_task_list'),
    path('detail/<int:task_id>/json/', views.task_detail_json, name='task_detail_json'),
    path('update_tasklist/', views.update_tasklist, name='update_task_list'),
]