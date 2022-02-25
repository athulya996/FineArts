from django.contrib import admin

# Register your models here.
from artsapp import models

admin.site.register(models.Login)
admin.site.register(models.Group)
admin.site.register(models.Teacher)
admin.site.register(models.Student)
admin.site.register(models.Program)
admin.site.register(models.ProgramRegistration)
admin.site.register(models.Result)

