from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from staff_attendance.models import Attendance, Staff
from .serializer import AttendanceCreateSerializer, AttendanceListSerializer, StaffListSerializer

@api_view(['POST'])
def attendance_create_api(request):
    serializer = AttendanceCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def attendance_list_api(request):
    attendances = Attendance.objects.all()
    serializer = AttendanceListSerializer(attendances, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def staff_list_api(request):
    staffs = Staff.objects.all()
    serializer = StaffListSerializer(staffs, many=True)
    return Response(serializer.data)
