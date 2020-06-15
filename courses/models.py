from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


STATUS_INACTIVE = 0
STATUS_ACTIVE = 1
STATUS_DRAFT = 2

STATUSES = ((STATUS_INACTIVE, 'неактивный'), (STATUS_ACTIVE, 'активный'), (STATUS_DRAFT, 'черновик'))


def replace_in_slugify(value):
    return value.replace(' ', '-')


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория курса'
        verbose_name_plural = 'Категории курсов'
        ordering = ['-created_at', 'order']

    name = models.CharField(max_length=255, null=False, blank=False)
    slug = AutoSlugField(max_length=250, populate_from='name',
                         unique_with=['name', 'created_at'],
                         slugify=replace_in_slugify)
    description = models.TextField()
    order = models.IntegerField(verbose_name='Порядок', null=False, blank=False, default=1000)

    status = models.PositiveSmallIntegerField(null=False, blank=False, choices=STATUSES, default=STATUS_ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_course_cat_user")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_course_cat_user")

    def __str__(self):
        return f'{self.name}'


class Course(models.Model):
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-created_at', 'order']

    SIMPLE_CHOICES = ((0, 'Нет'), (1, 'Да'))

    name = models.CharField(verbose_name='Название', max_length=255, null=False, blank=False)
    slug = AutoSlugField(verbose_name='Слаг', max_length=250, populate_from='name',
                         unique_with=['name', 'created_at'],
                         slugify=replace_in_slugify)
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(verbose_name='Превью', upload_to='media/courses/preview/%Y/%m/%d',
                                null=True, blank=True)
    has_certificate = models.SmallIntegerField(verbose_name='Наличие сертификата', null=False, blank=False,
                                               choices=SIMPLE_CHOICES, default=0)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE,
                                 related_name="course_category")
    started_at = models.DateField(verbose_name='Дата начала курса', null=True, blank=True)
    ended_at = models.DateField(verbose_name='Дата окончания курса', null=True, blank=True)
    order = models.IntegerField(verbose_name='Порядок', null=False, blank=False, default=1000)

    status = models.PositiveSmallIntegerField(verbose_name='Статус', null=False, blank=False, choices=STATUSES,
                                              default=STATUS_DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_course_user")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_course_user")

    def __str__(self):
        return f'Курс: {self.name}'

    def get_category_name(self):
        return self.category.name


class Lesson(models.Model):
    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'
        ordering = ['-created_at', 'order']

    course = models.ForeignKey(Course, verbose_name='Курс', on_delete=models.CASCADE, related_name="lesson_course")
    name = models.CharField(verbose_name='Название', max_length=255, null=False, blank=False)
    slug = AutoSlugField(verbose_name='Слаг', max_length=250, populate_from='name',
                         unique_with=['name', 'created_at'],
                         slugify=replace_in_slugify)
    description = models.TextField(verbose_name='Описание')
    purpose = models.TextField(verbose_name='Цели')
    order = models.IntegerField(verbose_name='Порядок', null=False, blank=False, default=1000)

    status = models.PositiveSmallIntegerField(verbose_name='Статус', null=False, blank=False, choices=STATUSES,
                                              default=STATUS_DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_lesson_user")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_lesson_user")

    def __str__(self):
        return f'Лекция: {self.name}'


class Task(models.Model):
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['-created_at']

    lesson = models.ForeignKey(Lesson, verbose_name='Лекция', on_delete=models.CASCADE, related_name="task_lesson")
    name = models.CharField(verbose_name='Название', max_length=255, null=False, blank=False)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    max_mark = models.IntegerField(verbose_name='Максимальная оценка')

    status = models.PositiveSmallIntegerField(verbose_name='Статус', null=False, blank=False, choices=STATUSES,
                                              default=STATUS_DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_task_user")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_task_user")

    def __str__(self):
        return f'{self.lesson.name}: {self.name}'


class TaskCriteria(models.Model):
    class Meta:
        verbose_name = 'Критерий оценки'
        verbose_name_plural = 'Критерии оценки'
        ordering = ['-created_at']

    task = models.ForeignKey(Task, verbose_name='Задание', on_delete=models.CASCADE, related_name="criteria_task")
    name = models.CharField(verbose_name='Название', max_length=255, null=False, blank=False)
    max_mark = models.IntegerField(verbose_name='Оценка')

    status = models.PositiveSmallIntegerField(verbose_name='Статус', null=False, blank=False, choices=STATUSES,
                                              default=STATUS_DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_task_criteria_user")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_task_criteria_user")

    def __str__(self):
        return f'{self.task.name}: {self.name}'
