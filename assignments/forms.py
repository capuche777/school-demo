"""
Form to create assign students to grade
"""
from django import forms

from .models import Assignment


class AssignmentForm(forms.ModelForm):
    """ Necessary field to create the assignment """
    class Meta:
        model = Assignment
        fields = ['student', 'grade', 'section']
