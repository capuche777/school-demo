"""
URL manager of Grades
"""
from django.urls import path

from .views import GradeListView, GradeCreate, GradeUpdate, GradeDelete

grades_patterns = [
    path('', GradeListView.as_view(), name='list'),
    path('add/', GradeCreate.as_view(), name='add'),
    path('edit/<int:pk>/', GradeUpdate.as_view(), name='edit'),
    path('delete/<int:pk>/', GradeDelete.as_view(), name='delete'),
]
