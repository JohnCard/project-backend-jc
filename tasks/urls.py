from django.urls import path
from .views import Tasks, CreateTask, MonoTask, TaskRetrieve

urlpatterns = [
    path('tasks', Tasks.as_view(), name='tasks'),
    path('task/', CreateTask.as_view(), name='create-task'),
    path('task/<int:id>', MonoTask.as_view(), name='task-update'),
    path('task-retrieve/<int:id>', TaskRetrieve.as_view(), name='task-get')
]