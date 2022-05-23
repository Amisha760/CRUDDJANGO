
from functools import partial
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,HttpResponse
import io
from rest_framework.parsers import JSONParser

from .serializers import StudentSerialzer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from .models import Student
# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        py_data=JSONParser().parse(stream)
        serializer=StudentSerialzer(py_data)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"data created"}
            json_msg=JSONRenderer().render(res)
            return HttpResponse(json_msg,content_type="application/json")

        json_error=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_error,content_type="application/json")
@csrf_exempt
def studentapi(request):
    if request.method=='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        py_data=JSONParser().parse(stream)
        id=py_data.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerialzer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type="application/json")
        
        stu=Student.objects.all()
        serializer=StudentSerialzer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type="application/json")

    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        py_data=JSONParser().parse(stream)
        id=py_data.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerialzer(stu,data=py_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"data updated"}
            json_msg=JSONRenderer().render(res)
            return HttpResponse(json_msg,content_type="application/json")

        json_error=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_error,content_type="application/json")
