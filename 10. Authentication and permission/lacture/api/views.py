from rest_framework import authentication
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

class StudentApi(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes=[AllowAny]
    permission_classes=[IsAdminUser]

    # Note :if you want to apply global authentication so go to your project directory and open setting.py

