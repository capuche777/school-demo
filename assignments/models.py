from django.db import models

from students.models import Student
from grades.models import Grade


class Assignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    section = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.student} - {self.grade} - {self.section}"
