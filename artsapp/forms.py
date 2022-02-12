import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from artsapp.models import Group, Teacher, Login


def phone_number_validator(value):
    if not re.compile(r'[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')


DEPARTMENT_CHOICES = (
    ('Select', 'Select'),
    ('Bsc cs', 'Bsc cs'),
    ('Bsc electronics', 'Bsc electronics'),
    ('BA english', 'Bsc english'),
    ('BA malayalam', 'Bsc malayalam'),
    ('Bcom', 'Bcom'),
    ('BCA', 'BCA'),
    ('Bsc mathematics', 'Bsc mathematics'),
)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


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
        fields = ('group_no', 'name', 'leader')


class UpdateGroup(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('group_no', 'name', 'leader')


class TeacherRegister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Please Enter a Valid Email')])

    class Meta:
        model = Teacher
        fields = ('name', 'contact_no', 'email', 'department', 'group')

class UpdateTeacher(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('name', 'contact_no', 'email', 'department', 'group')









