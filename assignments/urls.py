from django.contrib import admin
from django.urls import path

from .views import AssignmentListView, AssignmentCreate, AssignmentUpdate, AssignmentDelete

assignment_patterns = [
    path('', AssignmentListView.as_view(), name='list'),
    path('add/', AssignmentCreate.as_view(), name='add'),
    path('edit/<int:pk>/', AssignmentUpdate.as_view(), name='edit'),
    path('delete/<int:pk>/', AssignmentDelete.as_view(), name='delete'),
]
