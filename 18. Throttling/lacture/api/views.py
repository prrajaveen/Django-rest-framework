from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import authentication, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from api.throttling import StudentRateThrottle

# Go to your project Setting and you can change your jwt Default setting


class StudentApi(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle,UserRateThrottle]
    # throttle_classes=[AnonRateThrottle,StudentRateThrottle]
