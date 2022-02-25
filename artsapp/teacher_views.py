from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from artsapp.filters import StudentFilter, ProgramFilter, RegisterFilter, GroupFilter
from artsapp.forms import AddProgram, ProgramRegistrationForm
from artsapp.models import Student, Program, ProgramRegistration, Result, Group, StudentList


def teacher_home(request):
    return render(request, 'teacher_home.html')


def welcome_teacher(request):
    return render(request, 'teacher_temp/welcome_teacher.html')


@login_required(login_url='login_view')
def members(request):
    member = Student.objects.all().order_by('group')
    groupFilter = GroupFilter(request.GET, queryset=member)
    member = groupFilter.qs
    context = {
        'member': member,
        'groupFilter': groupFilter,
    }
    return render(request, 'teacher_temp/members.html', context)


@login_required(login_url='login_view')
def program_views(request):
    program = Program.objects.all()
    programFilter = ProgramFilter(request.GET, queryset=program)
    program = programFilter.qs
    context = {
        'program': program,
        'programFilter': programFilter,
    }
    return render(request, 'teacher_temp/program_views.html', context)


@login_required(login_url='login_view')
def program_updates(request,id):
    i = Program.objects.get(id=id)
    form = AddProgram(request.POST or None, instance=i)
    if form.is_valid():
        form.save()
        messages.info(request, 'Program Updated Successfully')
        return redirect('program_views')
    else:
        form = AddProgram(request.POST or None, instance=i)

    return render(request, 'teacher_temp/program_updates.html', {'form': form})


def add_program_teacher(request):
    program = ProgramRegistration.objects.all().order_by('-submitted_date')
    registerFilter = RegisterFilter(request.GET, queryset=program)
    program = registerFilter.qs

    context = {
        'program': program,
        'registerFilter': registerFilter,
    }
    return render(request, 'teacher_temp/add_program_teacher.html', context)


@login_required(login_url='login_view')
def teacher_register(request):
    program = ProgramRegistration.objects.all().order_by('-submitted_date')
    registerFilter = RegisterFilter(request.GET, queryset=program)
    program = registerFilter.qs
    context = {
        'program': program,
        'registerFilter':registerFilter
    }
    return render(request,'teacher_temp/teacher_register.html', context)


@login_required(login_url='login_view')
def program_result(request):
    program = Program.objects.all()
    programFilter = ProgramFilter(request.GET, queryset=program)
    program = programFilter.qs
    context = {
        'program': program,
        'programFilter': programFilter,
    }
    return render(request, 'teacher_temp/program_result.html', context)


@login_required(login_url='login_view')
def add_result(request, id):
    program = Program.objects.get(id=id)
    student = ProgramRegistration.objects.filter(program=program)

    if request.method == 'POST':
        mark = request.POST.get('mark')
        std = request.POST.get('student')

        qs = Result.objects.filter(student=std, program=program)
        if qs.exists():
            messages.info(request, 'Result of the Program {} Already Added for  this Candidate '.format(program))

        else:
            grp = ProgramRegistration.objects.get(id=std)

            Result(program=program, student=grp,
                   mark=mark, group=grp.group).save()
            grp_rslt_list = Result.objects.filter(program=program).order_by('-mark')[:3]
            i = 1
            for g in grp_rslt_list:
                g.rank = i
                g.save()
                i += 1

            grp_name = Group.objects.all()
            for grp in grp_name:
                total = 0
                grp_rslt_list = Result.objects.filter(group=grp, rank__in=(1, 2, 3))
                for i in grp_rslt_list:
                    total += i.mark
                    grp.total_score = total
                    grp.save()
            messages.info(request, 'Result Added Successfully ')
            return redirect('program_result')

    return render(request, 'teacher_temp/add_result.html', {'students': student, 'program': program})


@login_required(login_url='login_view')
def result_teacher(request):
    result = Program.objects.all()

    programFilter = ProgramFilter(request.GET, queryset=result)
    result = programFilter.qs

    context = {
        'result': result,
        'programFilter': programFilter,
    }
    return render(request, 'teacher_temp/result_teacher.html', context)


@login_required(login_url='login_view')
def results(request, id):
    program = Program.objects.get(id=id)
    result = Result.objects.filter(program=id).order_by('-mark')
    context = {
        'result': result,
        'program': program,

    }
    return render(request, 'teacher_temp/results.html', context)


@login_required(login_url='login_view')
def scoreboard(request):
    result = Group.objects.all().order_by('-total_score')
    return render(request, 'teacher_temp/scoreboard.html', {'result': result})


