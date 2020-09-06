from django.shortcuts import render, redirect

from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from courses.models import Course, STATUS_ACTIVE
from courses.forms import CourseForm


class AllCoursesListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses/index.html'
    paginate_by = 5
    queryset = Course.objects.filter(status=STATUS_ACTIVE)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_request_var'] = "page"
        return context


class MyCoursesListView(LoginRequiredMixin, ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses/index.html'
    paginate_by = 5

    def get_queryset(self):
        user_pk = self.request.user.pk
        user_groups = self.request.user.groups.all().values_list('name', flat=True)
        if 'teacher' in user_groups:
            return Course.objects.filter(group_course__teachers__pk=user_pk)
        if 'student' in user_groups:
            return Course.objects.filter(group_course__members__pk=user_pk)
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_request_var'] = "page"
        return context


class CourseDetailView(DetailView):
    template_name = 'courses/detail.html'
    model = Course
    queryset = Course.objects.filter(status=STATUS_ACTIVE).prefetch_related('lesson_course')


class CourseCreateView(GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('admin:index')
    template_name = 'courses/create.html'
    form_class = CourseForm
    group_required = [u"admins"]

    def get_success_url(self):
        return reverse('courses:index')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.updated_by = self.request.user
        obj.save()
        messages.success(self.request, 'Курс создан!')
        return redirect(self.get_success_url())


class CourseUpdateView(GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('admin:index')
    model = Course
    form_class = CourseForm
    template_name = "courses/update.html"
    context_object_name = 'course'
    group_required = [u"teacher", u"admins"]

    @staticmethod
    def get_detail_url(id):
        return reverse('courses:detail_view', args=[id])

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.updated_by = self.request.user
        obj.save()

        messages.info(self.request, 'Курс обновлен!')
        return redirect(self.get_detail_url(obj.id))


class CourseDeleteView(GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('admin:index')
    model = Course
    template_name = "courses/delete.html"
    success_url = reverse_lazy('courses:index')
    success_message = "Курс удален!"
    context_object_name = 'course'
    group_required = [u"admins"]

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)


def handler404(request, exception):
    return render(request, '404.html', locals())
