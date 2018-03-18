from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import StudentSerializer
from . models import Student


# Create your views here.
class StudentView(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer