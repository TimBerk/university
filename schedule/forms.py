from datetime import datetime

from django import forms
from django.contrib.auth.models import User

from .models import Group, Membership, List, Personal, STATUS_ACTIVE as SCHD_ACTIVE
from courses.models import Course, Lesson, STATUS_ACTIVE as CRS_ACTIVE


class MemberForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        try:
            users = User.objects.filter(groups__name='student')
            self.fields['member'].choices = [(None, '')] + [(user.pk, user.get_full_name()) for user in users]
        except:
            self.fields['member'].queryset = User.objects.none()


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PersonalForm, self).__init__(*args, **kwargs)
        try:
            users = User.objects.filter(groups__name='teacher')
            self.fields['teacher'].choices = [(None, '')] + [(user.pk, user.get_full_name()) for user in users]
        except:
            self.fields['teacher'].queryset = User.objects.none()


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = List
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        try:
            today = datetime.now()
            courses = Course.objects.filter(finished_at__gt=today, status=CRS_ACTIVE)
            lessons = Lesson.objects.filter(course__finished_at__gt=today, course__status=CRS_ACTIVE, status=CRS_ACTIVE)
            groups = Group.objects.filter(course__finished_at__gt=today, course__status=CRS_ACTIVE, status=SCHD_ACTIVE)
            users = User.objects.filter(groups__name='teacher')

            self.fields['course'].choices = [(None, '')] + [(course.pk, course.name) for course in courses]
            self.fields['lesson'].choices = [(None, '')] + [(lesson.pk, lesson.name) for lesson in lessons]
            self.fields['group'].choices = [(None, '')] + [(group.pk, group.name) for group in groups]
            self.fields['teacher'].choices = [(None, '')] + [(user.pk, user.get_full_name()) for user in users]

        except:
            self.fields['course'].queryset = Course.objects.none()
            self.fields['lesson'].queryset = Lesson.objects.none()
            self.fields['group'].queryset = Group.objects.none()
            self.fields['teacher'].queryset = User.objects.none()
