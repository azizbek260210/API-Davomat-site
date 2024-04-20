from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # --------------------------staff-------------------------
    path('', views.index, name='index'),
    path('create_staff/', views.create_staff, name='create_staff'),
    path('list_staff/', views.list_staff, name='list_staff'),
    path('detail_staff/<int:id>/', views.detail_staff, name='detail_staff'),
    path('edit_staff/<int:id>/', views.edit_staff, name = 'edit_staff'),
    path('delete_staff/<int:id>/', views.delete_staff, name='delete_staff'),

    # --------------------------attendance-------------------------
    path('list_attendance/', views.list_attendance, name='list_attendance'),
    
    # --------------------------profile-------------------------
    path('edit_profile/<int:id>/', views.edit_profile, name = 'edit_profile'),

    # -----------------login, logout-------------------------------
    path('log-in/', views.log_in, name='log_in'),
    path('log-out/', views.log_out, name='log_out'),
    ]