from functools import partial
import json
from django.db.models import constraints
from django.shortcuts import render
from rest_framework.serializers import Serializer
from .serializers import StudentSerializer
from api import serializers
from django.http import HttpResponse,JsonResponse
from .models import Student
import io
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
def student_list(request):
    details=Student.objects.all()
    serializer=StudentSerializer(details, many=True)
    return JsonResponse(serializer.data,safe=False)


@csrf_exempt
def create(request):
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        stu_detail=JSONParser().parse(stream)
        serializer=StudentSerializer(data=stu_detail)
        if serializer.is_valid():
            serializer.save()
            res={'sucess':'you have been seccussfully submited'}
            return JsonResponse(res,safe=False)
        return JsonResponse(serializer.errors,safe=False)

@csrf_exempt
def stu_update(request):
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'success':'secussfully updated'}
            return JsonResponse(res , safe=False)
        return JsonResponse(serializer.errors)


@csrf_exempt
def stu_delete(request):
    if request.method=='DELETE':
        json_data=request.body
        print(json_data)
        print(json_data)
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        studentobj=Student.objects.filter(pk=id)
        studentobj.delete()
        res={'success':'Data deleted'}
        return JsonResponse(res,safe=False)
        
