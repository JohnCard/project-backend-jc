from rest_framework.serializers import ModelSerializer
from accounts.serializers import Username
from .models import Task

class TaskSerializer(ModelSerializer):
    user = Username()

    class Meta:
        model = Task
        fields = ['id', 'name', 'user', 'due_date', 'priority', 'description', 'checked']

class CreateTask(ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'name', 'user', 'due_date', 'priority', 'description']

class UpdateTask(ModelSerializer):

    class Meta:
        model = Task
        fields = ['name', 'user', 'due_date', 'priority', 'description', 'checked']