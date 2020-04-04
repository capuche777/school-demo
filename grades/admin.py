from django.contrib import admin

from .models import Grade


class GradeAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')


admin.site.register(Grade, GradeAdmin)
