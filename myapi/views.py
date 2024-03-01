from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework  .generics import ListCreateAPIView
from .models import *
from .serializer import *



class Output(ListCreateAPIView):
    queryset=Attendance.objects.filter(Status=True)
    serializer_class=Attendanceserializer

