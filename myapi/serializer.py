from rest_framework import serializers 
from .models import *


class Attendanceserializer(serializers.ModelSerializer): 
    class Meta:
        model=Attendance
        fields='__all__'
        depth=2