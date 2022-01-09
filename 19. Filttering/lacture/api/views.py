from rest_framework import serializers
from api.models import Student
from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView

# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    # queryset=Student.objects.filter(passby='Teacher1')
    serializer_class=StudentSerializer
    def get_queryset(self):
        user=self.request.user
        return Student.objects.filter(passby=user)