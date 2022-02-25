from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Login(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class Group(models.Model):
    group_no = models.IntegerField()
    name = models.CharField(max_length=100)
    leader_name = models.CharField(max_length=100)
    total_score = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, primary_key=True, related_name='teacher')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, primary_key=True, related_name='student')
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    semester = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=200)
    rule = models.TextField(max_length=300)
    type = models.CharField(max_length=300)
    limitation_of_participation = models.IntegerField()

    def __str__(self):
        return self.name


class StudentList(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_list', null=True, )
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='student_list')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='student_list')


class ProgramRegistration(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='program_registration')
    # student = models.ForeignKey(Student,on_delete=models.CASCADE, related_name='program_registration')
    students = models.ManyToManyField(StudentList, related_name='program_registration')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='program_registration')
    submitted_date = models.DateField()


class Result(models.Model):
    program = models.ForeignKey(Program, on_delete=models.DO_NOTHING, related_name='result')
    student = models.ForeignKey(ProgramRegistration, on_delete=models.DO_NOTHING, related_name='result', )
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    mark = models.FloatField()
    rank = models.IntegerField(default=0)
