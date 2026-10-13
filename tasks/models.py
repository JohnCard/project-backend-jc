from django.utils.text import Truncator
from django.db import models
from helpers.models import TrackingModel
from django.conf import settings

# Create your models here.

class Task(TrackingModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    name = models.CharField(verbose_name='Task name', help_text='Type task name', max_length=50, unique=True, null=False, blank=False)
    description = models.TextField(verbose_name='Description', help_text='Type a description for this task', null=True, blank=True)
    checked = models.BooleanField(verbose_name='Completed', default=False)
    priority = models.CharField(
        max_length=10,
        default='Normal',
        choices=[
            ('Low', 'Baja'),
            ('Normal', 'Normal'),
            ('Medium', 'Media'),
            ('High', 'Alta'),
            ('Immediate', 'Inmediata')
        ]
    )
    due_date = models.DateTimeField(verbose_name='Due date', help_text='Type a due date (optional)', null=True, blank=True)
    # Orden manual de las tareas
    # position = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def short_description(self):
        return Truncator(self.description).chars(50)