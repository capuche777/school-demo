from django.contrib import admin
from django.urls import path, include

from .views import TeacherListView, TeacherCreate, TeachertDelete, TeacherUpdate

teacher_patterns = [
    path('', TeacherListView.as_view(), name='list'),
    path('add/', TeacherCreate.as_view(), name='add'),
    path('edit/<int:pk>/', TeacherUpdate.as_view(), name='edit'),
    path('delete/<int:pk>/', TeachertDelete.as_view(), name='delete'),
]
