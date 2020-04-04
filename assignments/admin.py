from django.contrib import admin

from .models import Assignment


class AssigmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'grade', 'section')


admin.site.register(Assignment, AssigmentAdmin)
