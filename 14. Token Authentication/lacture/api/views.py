from django.shortcuts import render
from rest_framework import viewsets
import rest_framework
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class StudentApi(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
