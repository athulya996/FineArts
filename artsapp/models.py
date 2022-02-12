from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Login(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class Group(models.Model):
    group_no = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    leader = models.CharField(max_length=100)
    total_score = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, primary_key=True, related_name='teacher')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=200)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
