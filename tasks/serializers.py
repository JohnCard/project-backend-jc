from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from accounts.serializers import Username
from accounts.models import User
from .models import Task

class TaskSerializer(ModelSerializer):
    user = Username()

    class Meta:
        model = Task
        fields = ['id', 'name', 'user', 'due_date', 'priority', 'description', 'checked']

class CreateTask(ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False
    )

    class Meta:
        model = Task
        fields = ['id', 'name', 'user', 'due_date', 'priority', 'description', 'checked']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = Username(instance.user).data
        return data

class UpdateTask(ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False
    )

    class Meta:
        model = Task
        fields = ['name', 'user', 'due_date', 'priority', 'description', 'checked']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = Username(instance.user).data
        return data