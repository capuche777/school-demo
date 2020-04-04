from django.contrib import admin
from django.urls import path, include

from .views import StudentListView, StudentCreate, StudentUpdate, StudentDelete

student_patterns = [
    path('', StudentListView.as_view(), name='list'),
    path('add/', StudentCreate.as_view(), name='add'),
    path('edit/<int:pk>/', StudentUpdate.as_view(), name='edit'),
    path('delete/<int:pk>/', StudentDelete.as_view(), name='delete'),
]
