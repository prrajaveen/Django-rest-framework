from rest_framework import authentication
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, DjangoModelPermissions, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from .custompermissions import MyPermission

class StudentApi(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes=[AllowAny]
    # permission_classes=[IsAdminUser]
    # permission_classes=[IsAuthenticatedOrReadOnly]
    permission_classes=[MyPermission]

    # Note :if you want to apply global authentication so go to your project directory and open setting.py

