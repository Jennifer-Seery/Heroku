from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentsSerializer
# Create your views here.

class StudentList(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentsSerializer(students,many=True)
        return Response(serializer.data)

    def post(self):
        pass