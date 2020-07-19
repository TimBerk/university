from django.db import models
from django.contrib.auth.models import User

from courses.models import Course, Lesson

STATUS_INACTIVE = 0
STATUS_ACTIVE = 1
STATUS_DRAFT = 2

STATUSES = ((STATUS_INACTIVE, 'неактивный'), (STATUS_ACTIVE, 'активный'), (STATUS_DRAFT, 'черновик'))


class InfoMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Group(InfoMixin):
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('-created_at',)

    name = models.CharField(verbose_name='Название', max_length=255)
    course = models.ForeignKey(Course, verbose_name='Курс', on_delete=models.CASCADE, related_name="group_course")
    members = models.ManyToManyField(
        User,
        through='Membership',
        through_fields=('group', 'person')
    )

    status = models.PositiveSmallIntegerField(verbose_name='Статус', choices=STATUSES, default=STATUS_DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_groups")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_groups")

    def __str__(self):
        return f'Группа: {self.name}'


class Membership(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class List(InfoMixin):
    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание лекций'
        ordering = ('-created_at', '-started_at')

    course = models.OneToOneField(Course, verbose_name='Курс', on_delete=models.CASCADE)
    lesson = models.OneToOneField(Lesson, verbose_name='Лекция', on_delete=models.CASCADE)
    teacher = models.OneToOneField(User, verbose_name='Преподаватель', on_delete=models.CASCADE)
    group = models.OneToOneField(Group, verbose_name='Группа', on_delete=models.CASCADE)

    started_at = models.DateTimeField(verbose_name='Начало')
    ended_at = models.DateTimeField(verbose_name='Конец')

    status = models.PositiveSmallIntegerField(choices=STATUSES, default=STATUS_DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_schedules")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_schedules")

    def __str__(self):
        return f'{self.course.name} ({self.group.name}) {self.started_at}'
