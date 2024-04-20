from django.shortcuts import render, redirect
from staff_attendance import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
import datetime


@login_required(login_url='dashboard:log_in')
def index(request):
    """-----asosiy sahifa------"""
    user = User.objects.last()

    context = {
        'user': user,
    }

    return render(request, 'dashboard/index.html', context)

# ---------------------------xodim------------------------------

@login_required(login_url='dashboard:log_in')
def create_staff(request):
    """-----staff yaratish------"""
    statuses = models.Staff.status.field.choices
    if request.method == 'POST':
        # try:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            status = request.POST.get('status')
            avatar = request.FILES.get('avatar')
            if request.POST.get('is_active') == 'on':
                is_active = True
            else:
                is_active = False
            models.Staff.objects.create(
                first_name=first_name,
                last_name=last_name,
                status=status,
                avatar=avatar,
                is_active=is_active,
                )
        #     messages.success(request, 'Xodim ma`lumotlari muvoffaqqiyatli yaratildi')
        # except:
        #     messages.error(request, 'Xodim ma`lumotlari yaratishda xatolik')
    context = {
        'statuses':statuses,
            }

    return render(request, 'dashboard/staff/create.html', context)


@login_required(login_url='dashboard:log_in')
def list_staff(request):
    staffs = models.Staff.objects.all()

    context = {
        'staffs': staffs,
    }

    return render(request, 'dashboard/staff/list.html', context)


@login_required(login_url='dashboard:log_in')
def detail_staff(request, id):
    staff = models.Staff.objects.get(id=id)
    context = {
        'staff': staff,
    }

    return render(request, 'dashboard/staff/detail.html', context)


@login_required(login_url='dashboard:log_in')
def edit_staff(request, id):
    """--------staff edit-------"""
    staff = models.Staff.objects.get(id=id)
    if request.method == 'POST':
        try:
            first_name = request.POST.get('first_name')
            lirst_name = request.POST.get('lirst_name')
            status = request.POST.get('status')
            avatar = request.FILES.get('avatar')
            models.Staff.objects.filter(id=id).update(
                first_name=first_name,
                lirst_name=lirst_name,
                status=status,
                avatar=avatar,
            )
            messages.success(request, 'Xodim ma`lumotlari muvaffaqqiyatli o`zgartirildi')
            return redirect('dashboard:detail_staff', staff.id)
        except:
            messages.error(request, 'Xodim ma`lumotlarini o`zgartirishda xatolik')

    return render(request, 'dashboard/staff/edit.html', context={'staff': staff})


@login_required(login_url='dashboard:log_in')
def delete_staff(request, id):
    """----xodimni o'chirish----"""
    try:
        models.Staff.objects.filter(id=id).delete()
        messages.success(request, 'Xodimning ma`lumotlari muvoffaqqiyatli o`chirildi')
        return redirect('dashboard:list_staff')
    except:
        messages.error(request, 'Xodimning ma`lumotlarini o`chirishda xatolik')
    return render(request, 'dashboard/staff/delete.html')

# ------------------------------Davomat------------------------------

@login_required(login_url='dashboard:log_in')
def list_attendance(request):
    attendances = models.Attendance.objects.all()
    context = {
        'attendances': attendances,
    }

    return render(request, 'dashboard/attendance/list.html', context)

# --------------------------------profil-------------------------------------

@login_required(login_url='dashboard:log_in')
def edit_profile(request, id):
    user = models.User.objects.get(id=id)
    if request.method == "POST":
        try:
            first_name = request.POST.get('first_name')  
            last_name = request.POST.get('last_name')
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request, 'Profil muvaffaqqiyatli o`zgartirildi')
            user.save()
        except:
            messages.error(request, 'Profil o`zgartirishda xatolik yuz berdi')
        return redirect('dashboard:index')
    context = {
        'user': user,
    }
    return render(request, 'dashboard/profile/edit.html', context)


# ------------------------------ login, logout ----------------------------

def log_in(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            messages.success(request, 'Xush kelibsiz!')
        except:
            messages.error(request, 'Xatolik')
        if user is not None:
            login(request, user)
            return redirect('dashboard:index')
        else:
            return render(request, 'dashboard/auth/login.html', {'error_message': 'Username yoki passwordd.'})
    else:
        return render(request, 'dashboard/auth/login.html')


@login_required(login_url='dashboard:log_in')
def log_out(request):
    """-----chiqish----"""
    logout(request)
    return redirect('dashboard:log_in')


