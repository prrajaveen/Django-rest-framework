from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import  viewsets


# Go to your project Setting and you can change your jwt Default setting

class StudentApi(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    