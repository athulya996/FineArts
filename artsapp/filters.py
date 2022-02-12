import django_filters
from django import forms
from django_filters import CharFilter

from artsapp.models import Teacher


class TeacherFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Teacher', 'class': 'form-control'}))

    class Meta:
        model = Teacher
        fields = ('name',)