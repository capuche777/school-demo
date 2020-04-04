"""
Form to create assign students to grade
"""
from django import forms
from .models import Grade


class GradeForm(forms.ModelForm):
    """ Necessary field to create the grade """
    class Meta:
        model = Grade
        fields = ['name', 'teacher']
