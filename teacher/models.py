from django.db import models
from django.contrib.auth.models import User

from courses.models import Task


class Student(models.Model):
    class Meta:
        verbose_name = 'Cтуденты'
        verbose_name_plural = 'Cтуденты'

    user = models.ForeignKey(User, verbose_name='Студент', on_delete=models.CASCADE, related_name="teacher_user")
    student = models.ForeignKey(Task, verbose_name='Задание', on_delete=models.CASCADE, related_name="teacher_student")
