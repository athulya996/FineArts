import random

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from artsapp.filters import TeacherFilter, StudentFilter, ProgramFilter, RegisterFilter
from artsapp.forms import AddGroup, UpdateGroup, LoginRegister, TeacherRegister, StudentRegister, UpdateTeacher, \
    AddProgram
from artsapp.models import Group, Teacher, Student, Program, Result, ProgramRegistration


def admin_home(request):
    return render(request, 'admin_home.html')


def welcome(request):
    return render(request, 'admin_temp/welcome.html')


@login_required(login_url='login_view')
def add_group(request):
    form = AddGroup()
    if request.method == 'POST':
        form = AddGroup(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Group Added Successful")
            return redirect('view_group')
    return render(request, 'admin_temp/add_group.html', {'form': form})


@login_required(login_url='login_view')
def view_group(request):
    group = Group.objects.all().order_by('-id')
    return render(request, 'admin_temp/view_group.html', {'group': group})


@login_required(login_url='login_view')
def update_group(request, id):
    i = Group.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateGroup(request.POST or None, instance=i)
        if form.is_valid():
            form.save()
            messages.info(request, "Group Updated Successfully")
            return redirect('view_group')
    else:
        form = UpdateGroup(request.POST or None, instance=i)
    return render(request, 'admin_temp/update_group.html', {'form': form})

@login_required(login_url='login_view')
def delete_group(request, id):
    i = Group.objects.get(id=id)
    if request.method == 'POST':
        i.delete()
        return redirect('view_group')
    else:
        return redirect('view_group')



@login_required(login_url='login_view')
def register_teacher(request):
    user_form = LoginRegister()
    teacher_form = TeacherRegister()
    if request.method == 'POST':
        login_register = LoginRegister(request.POST)
        teacher_form = TeacherRegister(request.POST)

        if login_register.is_valid() and teacher_form.is_valid():
            user = login_register.save(commit=False)
            user.is_teacher = True
            user.save()
            teacher = teacher_form.save(commit=False)
            teacher.user = user
            teacher.save()
            messages.info(request, "Student Registered Successfull")
            return redirect('view_teacher')
    return render(request, 'admin_temp/register_teacher.html', {'user_form': user_form, 'teacher_form': teacher_form})

@login_required(login_url='login_view')
def view_teacher(request):
    teacher = Teacher.objects.all().order_by('-user_id')
    teacherFilter = TeacherFilter(request.GET, queryset=teacher)
    teacher = teacherFilter.qs
    context = {
        'teacher': teacher,
        'teacherFilter': teacherFilter,
    }
    return render(request, 'admin_temp/view_teacher.html', context)

@login_required(login_url='login_view')
def update_teacher(request,user_id):
    i = Teacher.objects.get(user_id=user_id)
    if request.method == 'POST':
        form = UpdateTeacher(request.POST or None, instance=i)
        if form.is_valid():
            form.save()
            messages.info(request, "Teacher Updated Successfully")
            return redirect('view_teacher')
    else:
        form = UpdateTeacher(request.POST or None, instance=i)
    return render(request, 'admin_temp/update_teacher.html', {'form': form})

@login_required(login_url='login_view')
def delete_teacher(request,user_id):
    i = Teacher.objects.get(user_id=user_id)
    if request.method == 'POST':
        i.delete()
        messages.info(request, 'Teacher Deleted Successfully')
        return redirect('view_teacher')
    else:
        return redirect('view_teacher')

@login_required(login_url='login_view')
def register_student(request):
    user_form = LoginRegister()
    student_form = StudentRegister()
    if request.method == 'POST':
        login_register = LoginRegister(request.POST)
        student_form = StudentRegister(request.POST)
        if login_register.is_valid() and student_form.is_valid():
            user = login_register.save(commit=False)
            user.is_student = True
            user.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            messages.info(request, "Student Registered Successfull")
            return redirect('view_student')

    return render(request, 'admin_temp/register_student.html', {'user_form': user_form, 'student_form': student_form})


@login_required(login_url='login_view')
def view_student(request):
    student = Student.objects.all().order_by('-user_id')
    studentFilter = StudentFilter(request.GET, queryset=student)
    student = studentFilter.qs
    context = {
        'student': student,
        'studentFilter': studentFilter,
    }
    return render(request, 'admin_temp/view_student.html', context)


@login_required(login_url='login_view')
def assign_group(request,user_id):
    student = Student.objects.get(user_id=user_id)
    groups = Group.objects.all()
    random_group = random.choice(groups)
    student.group = random_group
    student.save()
    return redirect('view_student')


@login_required(login_url='login_view')
def update_student(request,user_id):
    i = Student.objects.get(user_id=user_id)
    if request.method == 'POST':
        form = StudentRegister(request.POST or None, instance=i)
        if form.is_valid():
            form.save()
            messages.info(request, "Student Updated Successfully")
            return redirect('view_student')
    else:
        form = StudentRegister(request.POST or None, instance=i)
    return render(request, 'admin_temp/update_student.html', {'form': form})

@login_required(login_url='login_view')
def delete_student(request,user_id):
    i = Student.objects.get(user_id=user_id)
    if request.method == 'POST':
        i.delete()
        messages.info(request, 'Student Deleted Successfully')
        return redirect('view_student')
    else:
        return redirect('view_student')



@login_required(login_url='login_view')
def add_program(request):
    form = AddProgram()
    if request.method == 'POST':
        form = AddProgram(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Program Added Successfully')
            return redirect('view_program')
    return render(request, 'admin_temp/add_program.html', {'form': form})


@login_required(login_url='login_view')
def view_program(request):
    program = Program.objects.all().order_by('-id')
    programFilter = ProgramFilter(request.GET, queryset=program)
    program = programFilter.qs
    context = {
        'program': program,
        'programFilter': programFilter,
    }
    return render(request, 'admin_temp/view_program.html', context)

@login_required(login_url='login_view')
def update_program(request, id):
    i = Program.objects.get(id=id)
    form = AddProgram(request.POST or None, instance=i)
    if form.is_valid():
        form.save()
        messages.info(request, 'Program Updated Successfully')
        return redirect('view_program')
    else:
        form = AddProgram(request.POST or None, instance=i)

    return render(request, 'admin_temp/update_program.html', {'form': form})


@login_required(login_url='login_view')
def delete_program(request, id):
    i = Program.objects.get(id=id)
    if request.method == 'POST':
        i.delete()
        messages.info(request, 'Program Deleted Successfully')
        return redirect('view_program')
    else:
        return redirect('view_program')



@login_required(login_url='login_view')
def program_register(request):
    program = ProgramRegistration.objects.all().order_by('-submitted_date')
    registerFilter = RegisterFilter(request.GET, queryset=program)
    program = registerFilter.qs

    context = {
        'program': program,
        'registerFilter': registerFilter,
    }
    return render(request, 'admin_temp/program_register.html', context)





@login_required(login_url='login_view')
def result_list(request):
    result = Program.objects.all()

    programFilter = ProgramFilter(request.GET, queryset=result)
    result = programFilter.qs

    context = {
        'result': result,
        'programFilter': programFilter,
    }
    return render(request, 'admin_temp/result_list.html', context)


@login_required(login_url='login_view')
def view_result(request, id):
    program = Program.objects.get(id=id)
    result = Result.objects.filter(program=id).order_by('-mark')
    context = {
        'result': result,
        'program': program,

    }
    return render(request, 'admin_temp/view_result.html', context)

@login_required(login_url='login_view')
def score_board(request):
    result = Group.objects.all().order_by('-total_score')

    return render(request, 'admin_temp/score_board.html', {'result': result})




