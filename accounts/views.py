from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import User
from .serializers import UserSerializer, Username

# Create your views here.

class Users(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UsernameList(ListAPIView):
    serializer_class = Username
    queryset = User.objects.all()