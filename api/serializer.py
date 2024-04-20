from rest_framework import serializers
from staff_attendance.models import Attendance, Staff

class AttendanceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


class AttendanceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


class StaffListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
