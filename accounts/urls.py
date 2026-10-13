from rest_framework.urls import path
from .views import Users, UsernameList

urlpatterns = [
    path('users', Users.as_view(), name='users'),
    path('username-list', UsernameList.as_view(), name='username-list')
]