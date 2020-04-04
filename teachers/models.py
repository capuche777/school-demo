from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.CharField(max_length=1, choices=GENDER)

    def __str__(self):
        return f"{self.name} {self.last_name}"
