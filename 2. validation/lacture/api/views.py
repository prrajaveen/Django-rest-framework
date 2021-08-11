from functools import partial
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .models import Student
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
import io

# Create your views here.

#for display all student
def stu_list(request):
    data=Student.objects.all()
    serializer=StudentSerializer(data,many=True)
    return JsonResponse(serializer.data,safe=False)

#for Add new student
@csrf_exempt
def stu_create(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'Success':'data has been secussfully Created'}
            return JsonResponse(res,safe=False)
        return JsonResponse(serializer.errors,safe=False)


#for update Existing student
@csrf_exempt
def stu_update(request):
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        stu_id=pythondata.get('id')
        stu=Student.objects.get(id=stu_id)
        serializer=StudentSerializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'Success':'Your data has been secussfully updated'}
            return JsonResponse(res,safe=False)
        return JsonResponse(serializer.errors)

#for Delete a particular student
@csrf_exempt
def stu_delete(request):
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythoddata=JSONParser().parse(stream)
        stu_id=pythoddata.get('id')
        stu_object=Student.objects.get(id=stu_id)
        stu_object.delete()
        res={'Sucess':'Your data has been secussfully deleted'}
        return JsonResponse(res,safe=False)