from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from core.views import Index
from students.urls import student_patterns
from teachers.urls import teacher_patterns
from grades.urls import grades_patterns
from assignments.urls import assignment_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', Index.as_view()),
    path('students/', include((student_patterns, 'students'), namespace='students')),
    path('teachers/', include((teacher_patterns, 'teachers'), namespace='teachers')),
    path('grades/', include((grades_patterns, 'grades'), namespace='grades')),
    path('assignments/', include((assignment_patterns, 'assignments'), namespace='assignments')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
