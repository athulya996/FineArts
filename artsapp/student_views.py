import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from artsapp.filters import StudentFilter, ProgramFilter, GroupFilter
from artsapp.models import Student, Program, ProgramRegistration, StudentList, Result, Group


def student_home(request):
    return render(request, 'student_home.html')


def welcome_student(request):
    return render(request, 'student_temp/welcome_student.html')

@login_required(login_url='login_view')
def group_view(request):
    student = Student.objects.get(user=request.user)
    member = Student.objects.filter(user=student.user)
    groupFilter = StudentFilter(request.GET, queryset=member)
    member = groupFilter.qs
    context = {
        'member': member,
        'groupFilter': GroupFilter
    }
    return render(request, 'student_temp/group_view.html', context)


@login_required(login_url='login_view')
def program_student(request):
    program = Program.objects.all()
    programFilter = ProgramFilter(request.GET, queryset=program)
    program = programFilter.qs
    context = {
        'program': program,
        'programFilter': programFilter
    }
    return render(request, 'student_temp/program_student.html', context)


@login_required(login_url='login_view')
def register_program(request, id):
    u = Student.objects.get(user=request.user)
    grp = u.group
    if grp == None or grp == "":
        messages.info(request, "You Haven't Assigned to Any Group yet")
        return redirect('program_student')
    else:
        program = Program.objects.get(id=id)
        limit = program.limitation_of_participation
        limit1 = []
        for i in range(limit):
            limit1.append(i)
            student = Student.objects.filter(group=u.group)
            context = {
                 'program': program,
                 'students': student,
                 'limit':limit1
            }
            if request.method == 'POST':
                std = request.POST.getlist('student')
                if len(std) == len(set(std)):
                    reg_qs = ProgramRegistration.objects.filter(group=grp , program=program)
                    if reg_qs.exists():
                        messages.info(request,"Your Group {} Already Registered for the Program {}".format(grp, program))
                        return redirect('program_student')
                    if len(std) > limit:
                        messages.info(request, 'Maximum no of group members is {}'.format(limit))
                    else:
                        obj = ProgramRegistration.objects.create(program=program, submitted_date=datetime.date.today(), group=grp,)
                        for i in std:
                            id = int(i)
                            student_list, created = StudentList.objects.get_or_create(
                                program=program,
                                group=grp,
                                student=Student.objects.get(user_id=id)
                            )
                            obj.students.add(student_list)
                            messages.info(request, 'Successfully Registered for Program')
                            return redirect('registered_program')
        else:
            messages.info(request, "You Can't Select Same Students ")
    return render(request, 'student_temp/register_program.html', context)


@login_required(login_url='login_view')
def registered_program(request):
    student = Student.objects.get(user=request.user)
    program = ProgramRegistration.objects.filter(students__student=student)
    context = {
        'program': program
    }
    return render(request, 'student_temp/registered_program.html', context)


@login_required(login_url='login_view')
def result_student(request):
    result = Program.objects.all()

    programFilter = ProgramFilter(request.GET, queryset=result)
    result = programFilter.qs

    context = {
        'result': result,
        'programFilter': programFilter,
    }
    return render(request, 'student_temp/result_student.html', context)


@login_required(login_url='login_view')
def results_program(request, id):
    program = Program.objects.get(id=id)
    result = Result.objects.filter(program=id).order_by('-mark')
    context = {
        'result': result,
        'program': program,

    }
    return render(request, 'student_temp/results_program.html', context)


@login_required(login_url='login_view')
def student_scoreboard(request):
    result = Group.objects.all().order_by('-total_score')
    return render(request, 'student_temp/student_scoreboard.html', {'result': result})




