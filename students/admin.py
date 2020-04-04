from django.contrib import admin

from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'gender', 'birthdate')


admin.site.register(Student, StudentAdmin)
