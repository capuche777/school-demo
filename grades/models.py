"""
Model to manage Grades
"""
from django.db import models

from teachers.models import Teacher


class Grade(models.Model):
    """ Assign teacher to grade """
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
