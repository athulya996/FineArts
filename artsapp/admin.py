from django.contrib import admin

# Register your models here.
from artsapp import models

admin.site.register(models.Login)
admin.site.register(models.Teacher)
