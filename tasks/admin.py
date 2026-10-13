from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'checked', 'due_date', 'priority')
    search_fields = ('id', 'name', 'checked', 'due_date', 'priority')
    list_filter = ('id', 'name', 'checked', 'due_date', 'priority')
    ordering = ['id', 'created_at']

admin.site.register(Task, TaskAdmin)