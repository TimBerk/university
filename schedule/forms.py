from django import forms
from django.contrib.auth.models import User

from .models import Membership


class MemberForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        try:
            users = User.objects.filter(groups__name='student', membership__isnull=False)
            self.fields['member'].choices = [(None, '')] + [(user.pk, user.get_full_name()) for user in users]
        except:
            self.fields['member'].queryset = User.objects.none()


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PersonalForm, self).__init__(*args, **kwargs)
        try:
            users = User.objects.filter(groups__name='teacher')
            self.fields['teacher'].choices = [(None, '')] + [(user.pk, user.get_full_name()) for user in users]
        except:
            self.fields['teacher'].queryset = User.objects.none()
