import datetime
import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import DateInput

from artsapp.models import Group, Teacher, Login, Student, Program, ProgramRegistration, Result


def phone_number_validator(value):
    if not re.compile(r'[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'

SEMESTER_CHOICES = (
    ('Select', 'Select'),
    ('First Semester', 'First Semester'),
    ('Second Semester', 'Second Semester'),
    ('Third Semester', 'Third Semester'),
    ('Fourth Semester', 'Fourth Semester'),
    ('Fifth Semester', 'Fifth Semester'),
    ('Sixth Semester', 'Sixth Semester'),
)



DEPARTMENT_CHOICES = (
    ('Select', 'Select'),
    ('Bsc cs', 'Bsc cs'),
    ('Bsc electronics', 'Bsc electronics'),
    ('BA english', 'BA english'),
    ('BA malayalam', 'BA malayalam'),
    ('Bcom', 'Bcom'),
    ('BCA', 'BCA'),
    ('Bsc mathematics', 'Bsc mathematics'),
)





class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class AddGroup(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('group_no', 'name', 'leader_name')


class UpdateGroup(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('group_no', 'name', 'leader_name')


class TeacherRegister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Please Enter a Valid Email')])


    class Meta:
        model = Teacher
        fields = ('name', 'contact_no', 'email', 'department', 'group')


class UpdateTeacher(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Please Enter a Valid Email')])

    class Meta:
        model = Teacher
        fields = ('name', 'contact_no', 'email', 'department', 'group')


class StudentRegister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    semester = forms.ChoiceField(choices=SEMESTER_CHOICES)
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Please Enter a Valid Email')])

    class Meta:
        model = Student
        fields = ('name', 'contact_no', 'email', 'roll_no', 'semester', 'department', 'group')


class UpdateStudent(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    semester = forms.ChoiceField(choices=SEMESTER_CHOICES)
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$', message='Please Enter a Valid Email')])

    class Meta:
        model = Student
        fields = ('name', 'contact_no', 'email', 'semester', 'department', 'group')


TYPE_CHOICES = (
    ('Individual', 'Individual'),
    ('Group', 'Group'),
)


class AddProgram(forms.ModelForm):
    type = forms.ChoiceField(choices=TYPE_CHOICES)

    class Meta:
        model = Program
        fields = ('name', 'rule', 'type', 'limitation_of_participation')

class ProgramRegistrationForm(forms.ModelForm):
    submitted_date = forms.DateField(widget=DateInput)
    student = forms.ModelMultipleChoiceField(queryset=Student.objects.all())

    class Meta:
        model = ProgramRegistration
        fields = ('program', 'submitted_date', 'students')


class ResultForm(forms.ModelForm):
    mark = forms.IntegerField()

    class Meta:
        model = Result
        fields = ('program', 'student', 'mark')








