

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            if user.is_teacher:
                return redirect('teacher_home')
            if user.is_student:
                return redirect('student_home')
        else:
            messages.info(request, "Invalid Credentials")
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login_view')
