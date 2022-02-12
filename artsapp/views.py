

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from artsapp.forms import LoginForm



def home(request):
    return render(request, 'home.html')


def login(request):
    form = LoginForm()
    if request.method == 'post':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                if user.is_staff:
                    return  redirect('admin_home')
                if user.is_teacher:
                    return redirect('teacher_home')
                if user.is_student:
                    return redirect('student_home')
                else:
                    messages.info(request,"Invalid Credentials")
    return render(request, 'login.html', {'form': form})


def admin_home(request):
    return render(request, 'admin_home.html')


