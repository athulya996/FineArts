
from django.contrib import messages

from django.shortcuts import render, redirect

from artsapp.filters import TeacherFilter
from artsapp.forms import AddGroup, UpdateGroup, LoginRegister, TeacherRegister
from artsapp.models import Group, Teacher






def add_group(request):
    form = AddGroup()
    if request.method == 'POST':
        form = AddGroup(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Group Added Successful")
            return redirect('view_group')
    return render(request, 'admintemp/add_group.html', {'form': form})


def view_group(request):
    group = Group.objects.all()
    return render(request, 'admintemp/view_group.html', {'group': group})


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
    return render(request, 'admintemp/update_group.html', {'form': form})


def delete_group(request, id):
    i = Group.objects.get(id=id)
    if request.method == 'POST':
        i.delete()
        return redirect('view_group')
    else:
        return redirect('view_group')




def register_teacher(request):
    login_form = LoginRegister()
    teacher_form = TeacherRegister()
    context = {
        'login_form': login_form,
        'teacher_form': teacher_form
    }
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        teacher_form = TeacherRegister(request.POST)
        print(request.POST['name'])
        if login_form.is_valid() and teacher_form.is_valid():
            user = login_form.save(commit=False)
            user.is_teacher = True
            user.save()
            teacher = teacher_form.save(commit=False)
            teacher.user = user
            teacher.save()
            messages.info(request, "Student Registered Successfull")
            return redirect('view_teacher')
        context = {
            'login_form': login_form,
            'teacher_form': teacher_form
        }
    return render(request, 'admintemp/register_teacher.html', context)


def view_teacher(request):
    teacher = Teacher.objects.all()
    teacherFilter = TeacherFilter(request.GET, queryset=teacher)
    teacher = teacherFilter.qs
    context = {
        'teacher': teacher,
        'teacherFilter': teacherFilter,
    }
    return render(request, 'admintemp/view_teacher.html', context)


def update_teacher(request,user_id):
    i = Teacher.objects.get(user_id=user_id)
    if request.method == 'POST':
        form = TeacherRegister(request.POST or None, instance=i)
        if form.is_valid():
            form.save()
            messages.info(request, "Teacher Updated Successfully")
            return redirect('view_teacher')
    else:
        form = TeacherRegister(request.POST or None, instance=i)
    return render(request, 'admintemp/update_teacher.html', {'form': form})


def delete_teacher(request,user_id):
    i = Teacher.objects.get(user_id=user_id)
    if request.method == 'POST':
        i.delete()
        messages.info(request, 'Teacher Deleted Successfully')
        return redirect('view_teacher')
    else:
        return redirect('view_teacher')










