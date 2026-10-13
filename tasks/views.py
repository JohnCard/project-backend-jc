from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .serializers import TaskSerializer, CreateTask, UpdateTask
from .models import Task
from helpers.pagination import BasicPagination

# Create your views here.

class Tasks(ListAPIView):
    serializer_class = TaskSerializer
    pagination_class = BasicPagination
    queryset = Task.objects.all()
    # def get_queryset(self):
    #     return Tasks.objects.all().filter(user=self.request.user)

class CreateTask(CreateAPIView):
    serializer_class = CreateTask
    queryset = Task.objects.all()

class MonoTask(RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateTask
    
    lookup_field = 'id'

    def get_queryset(self):
        return Task.objects.filter(id=self.kwargs['id'])

class TaskRetrieve(RetrieveAPIView):
    serializer_class = TaskSerializer

    lookup_field = 'id'

    def get_queryset(self):
        return Task.objects.filter(id=self.kwargs['id'])