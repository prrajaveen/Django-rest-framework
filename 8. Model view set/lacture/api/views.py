from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

class StudentApi(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def destroy(self, request, *args,pk, **kwargs):
        stu=Student.objects.get(id=pk)
        stu.delete()
        return Response({'success':'data deleted'})