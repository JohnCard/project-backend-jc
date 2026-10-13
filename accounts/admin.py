from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'balance', 'email', 'is_staff')
    search_fields = ('id', 'username', 'first_name', 'last_name', 'balance', 'email', 'is_staff')
    list_filter = ('id', 'username', 'first_name', 'last_name', 'balance', 'email', 'is_staff')
    ordering = ['created_at']

admin.site.register(User, UserAdmin)