from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q

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
        through_fields=('group', 'member'),
        related_name='group_members'
    )

    teachers = models.ManyToManyField(
        User,
        through='Personal',
        through_fields=('group', 'teacher'),
        related_name='group_teachers'
    )

    status = models.PositiveSmallIntegerField(verbose_name='Статус', choices=STATUSES, default=STATUS_DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_groups")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_groups")

    def __str__(self):
        return f'Группа: {self.name}'


class Membership(models.Model):
    member = models.ForeignKey(User, verbose_name='Студент', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
        unique_together = ('member', 'group',)

    def __str__(self):
        return f'{self.member.get_full_name()} ({self.group.name})'


class Personal(models.Model):
    teacher = models.ForeignKey(User, verbose_name='Преподаватель', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        unique_together = ('teacher', 'group',)

    def __str__(self):
        return f'{self.teacher.get_full_name()} ({self.group.name})'


class List(InfoMixin):
    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание лекций'
        ordering = ('-created_at', '-started_at')
        unique_together = ('course', 'lesson', 'teacher', 'group', 'started_at')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', related_name='schedule_course')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Лекция', related_name='schedule_lesson')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Преподаватель',
                                related_name='schedule_teacher')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа', related_name='schedule_group')

    started_at = models.DateTimeField(verbose_name='Начало')
    ended_at = models.DateTimeField(verbose_name='Конец')

    status = models.PositiveSmallIntegerField(verbose_name='Статус', choices=STATUSES, default=STATUS_DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_schedules")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_schedules")

    def __str__(self):
        return f'{self.course.name} ({self.group.name}) {self.started_at}'

    def clean(self):
        lesson_ended = List.objects.filter(started_at__lt=self.ended_at, ended_at__gte=self.ended_at).filter(
            Q(group=self.group) | Q(teacher=self.teacher))
        lesson_started = List.objects.filter(started_at__gte=self.started_at, ended_at__lt=self.started_at).filter(
            Q(group=self.group) | Q(teacher=self.teacher))

        if len(lesson_ended) > 0:
            for lesson in lesson_ended:
                if lesson.teacher == self.teacher:
                    raise ValidationError({'teacher': ["У выбранного преподавателя уже есть лекция в выбранное время"]})

                if lesson.group == self.group:
                    raise ValidationError({'group': ["У выбранной группы уже есть лекция в выбранное время"]})

        if len(lesson_started) > 0:
            for lesson in lesson_started:
                if lesson.teacher == self.teacher:
                    raise ValidationError({'teacher': ["У выбранного преподавателя уже есть лекция в выбранное время"]})
                if lesson.group == self.group:
                    raise ValidationError({'group': ["У выбранной группы уже есть лекция в выбранное время"]})
