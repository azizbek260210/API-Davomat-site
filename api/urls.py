from django.urls import path
from . import views

urlpatterns = [
    path('staff-list/', views.staff_list_api, name='staff-list'),
    path('attendance-create/', views.attendance_create_api, name='attendance-create'),
    path('attendance-list/', views.attendance_list_api, name='attendance-list'),
]
