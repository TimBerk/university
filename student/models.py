from django.db import models
from django.contrib.auth.models import User

from courses.models import Task

STATUS_NOT_STARTED = 0
STATUS_NOT_PASSED = 1
STATUS_PASSED = 2
STATUS_CHECKED = 3

STATUSES_HOMEWORK = (
    (STATUS_NOT_STARTED, 'не начат'),
    (STATUS_NOT_PASSED, 'не пройден'),
    (STATUS_PASSED, 'пройден'),
    (STATUS_CHECKED, 'на проверке')
)


class InfoMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Homework(InfoMixin):
    class Meta:
        verbose_name = 'Задания студента'
        verbose_name_plural = 'Задания студента'

    user = models.ForeignKey(User, verbose_name='Студент', on_delete=models.CASCADE, related_name="student_user")
    task = models.ForeignKey(Task, verbose_name='Задание', on_delete=models.CASCADE, related_name="student_task")
    score = models.IntegerField(verbose_name='Оценка', default=0)

    status = models.PositiveSmallIntegerField(verbose_name='Статус', choices=STATUSES_HOMEWORK,
                                              default=STATUS_NOT_STARTED)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_homework")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_homework")

    def __str__(self):
        return f'{self.user.username} {self.task.name} homework'
