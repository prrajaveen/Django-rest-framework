from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView,RetrieveAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView    
from rest_framework.throttling import ScopedRateThrottle  

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='stu'
 

class StudentCreate(CreateAPIView):
    queryset=Student.objects.all
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]

class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]

class StudentRetrive(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modifystu'

class StudentDelete(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]