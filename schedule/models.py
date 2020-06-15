from django.db import models
from django.contrib.auth.models import User

from courses.models import Course, Lesson


STATUS = ((0, 'неактивный'), (1, 'активный'), (2, 'черновик'))


class Group(models.Model):
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['-created_at']

    name = models.CharField(verbose_name='Название', max_length=255, null=False, blank=False)

    status = models.SmallIntegerField(verbose_name='Статус', null=False, blank=False, choices=STATUS, default=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_group_user")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_group_user")

    def __str__(self):
        return f'Группа: {self.name}'


class List(models.Model):
    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание лекций'
        ordering = ['-created_at', '-started_at']

    course = models.OneToOneField(Course, verbose_name='Курс', on_delete=models.CASCADE)
    lesson = models.OneToOneField(Lesson, verbose_name='Лекция', on_delete=models.CASCADE)
    teacher = models.OneToOneField(User, verbose_name='Преподаватель', on_delete=models.CASCADE)
    group = models.OneToOneField(Group, verbose_name='Группа', on_delete=models.CASCADE)

    started_at = models.DateField(verbose_name='Начало', null=False, blank=False)
    ended_at = models.DateField(verbose_name='Конец', null=False, blank=False)

    status = models.SmallIntegerField(null=False, blank=False, choices=STATUS, default=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_schedule_user")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_schedule_user")

    def __str__(self):
        return f'{self.course.name} ({self.course.name}) {self.started_at}'
