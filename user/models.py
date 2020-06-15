from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from autoslug import AutoSlugField


STATUS_INACTIVE = 0
STATUS_ACTIVE = 1
STATUS_DRAFT = 2

STATUSES = ((STATUS_INACTIVE, 'неактивный'), (STATUS_ACTIVE, 'активный'), (STATUS_DRAFT, 'черновик'))


def replace_in_slugify(value):
    return value.replace(' ', '-')


class Scope(models.Model):
    class Meta:
        verbose_name = 'Сфера деятельности'
        verbose_name_plural = 'Сферы деятельности'
        ordering = ['-created_at', 'order']

    name = models.CharField(verbose_name='Название', max_length=255, null=False, blank=False)
    slug = AutoSlugField(verbose_name='Слаг', max_length=250, populate_from='name',
                         unique_with=['name', 'created_at'],
                         slugify=replace_in_slugify)
    order = models.IntegerField(verbose_name='Порядок', null=False, blank=False, default=1000)

    status = models.PositiveSmallIntegerField(verbose_name='Статус', null=False, blank=False, choices=STATUSES,
                                              default=STATUS_ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_scope_user")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_scope_user")

    def __str__(self):
        return f'{self.name}'


class Skill(models.Model):
    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
        ordering = ['order', 'name', '-created_at']

    name = models.CharField(verbose_name='Название', max_length=255, null=False, blank=False)
    slug = AutoSlugField(verbose_name='Слаг', max_length=250, populate_from='name',
                         unique_with=['name', 'created_at'],
                         slugify=replace_in_slugify)
    order = models.IntegerField(verbose_name='Порядок', null=False, blank=False, default=1000)

    status = models.PositiveSmallIntegerField(verbose_name='Статус', null=False, blank=False, choices=STATUSES,
                                              default=STATUS_ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_skill_user")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_skill_user")

    def __str__(self):
        return f'{self.name}'


class Profile(models.Model):
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'

    GENDER = ((1, 'мужской'), (2, 'женский'))
    ROLES = ((1, 'Пользователь'), (2, 'Менеджер'), (3, 'Студент'), (4, 'Преподаватель'), (5, 'Администратор'))
    QUALIFICATION = (
        (0, 'Не указана'),
        (1, 'Стажер (Intern)'),
        (2, 'Младший (Junior)'),
        (3, 'Средний (Middle)'),
        (4, 'Старший (Senior)'),
        (5, 'Ведущий (Leaf)')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.SmallIntegerField(verbose_name='Роль', null=False, blank=False, choices=ROLES, default=1)
    gender = models.SmallIntegerField(verbose_name='Пол', null=True, blank=True, choices=GENDER, default=1)
    qualification = models.SmallIntegerField(verbose_name='Квалификация', null=True, blank=True,
                                             choices=QUALIFICATION, default=0)
    birth_date = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=20, null=True, blank=True)
    location = models.CharField(verbose_name='Город', max_length=70, null=True, blank=True)
    avatar = models.ImageField(verbose_name='Аватар', upload_to='media/avatars/%Y/%m/%d', null=True, blank=True)

    scope = models.OneToOneField(Scope, verbose_name='Обдасть деятельности', on_delete=models.CASCADE, null=True)
    skills = models.ManyToManyField(Skill, verbose_name='Навыки')

    def __str__(self):
        return f'{self.user.username} user profile'


@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_student_profile(sender, instance, **kwargs):
    instance.profile.save()
