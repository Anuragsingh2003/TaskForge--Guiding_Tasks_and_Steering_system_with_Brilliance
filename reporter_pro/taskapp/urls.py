from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('usr_dash/', views.usr_dash, name='usr_dash'),
    path('user_tasks/', views.user_tasks, name='user_tasks'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('user_login/', views.user_login, name='user_login'),
    path('admin_d/', views.admin_d, name='admin_d'),
    path('manage_task/', views.manage_task, name='manage_task'),
    path('create_task/', views.create_task, name='create_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('del/<int:task_id>/', views.del_task, name='del_task'),
    path('status_updates/<int:task_id>/', views.status_updates, name='status_updates'),
    path('leave_list/', views.leaves_list, name='leaves_list'),
    path('leave_create/', views.create_leave, name='create_leave'),
    path('accept_leave/<int:leave_id>/', views.accept_leave, name='accept_leave'),
    path('reject_leave/<int:leave_id>/', views.reject_leave, name='reject_leave'),
    path('full_message/<int:leave_id>/', views.full_message_view, name='full_message'),
    path('task_desc/<int:task_id>/', views.task_desc, name='task_desc'),
    path('task_more/<int:task_id>/', views.task_more, name='task_more'),
    path('leave_status/', views.leave_status, name='leave_status'),


]
