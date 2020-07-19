from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, get_object_or_404

from student.forms.signup import SignUpForm
from user.models import Profile

ROLE_TEACHER = 4


class SignupView(CreateView):
    template_name = 'student/signup.html'
    form_class = SignUpForm

    def get_success_url(self):
        return reverse('courses:index')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        profile = get_object_or_404(Profile, pk=obj.pk)
        profile.role = ROLE_TEACHER
        profile.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)

        messages.success(self.request, 'Вы зарегестрированы!')
        return redirect(self.get_success_url())


@login_required(login_url='/teacher/login/')
def logout_view(request):
    logout(request)
