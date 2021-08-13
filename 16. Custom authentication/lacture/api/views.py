from rest_framework import authentication
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, DjangoModelPermissions, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from api.customauth import CustomAuthentication

class StudentApi(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[CustomAuthentication]
    permission_classes = [IsAuthenticated]

