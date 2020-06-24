from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from courses.models import Course
from courses.forms import CourseForm


class AllCoursesListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses/index.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_request_var'] = "page"
        return context


class CourseDetailView(DetailView):
    template_name = 'courses/detail.html'
    model = Course


class CourseCreateView(LoginRequiredMixin, CreateView):
    login_url = '/admin/'
    template_name = 'courses/create.html'
    form_class = CourseForm

    def get_success_url(self):
        return reverse('courses:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request):
        current_user = request.user if request.user else None
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid() and not current_user.is_anonymous:
            form.cleaned_data['created_by'] = current_user
            form.cleaned_data['updated_by'] = current_user
            Course.objects.create(**form.cleaned_data)
            messages.success(request, 'Курс создан!')
            return redirect(self.get_success_url())
        return render(request, 'courses/create.html', context={'form': form})


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/admin/'
    model = Course
    form_class = CourseForm
    template_name = "courses/update.html"

    @staticmethod
    def get_detail_url(id):
        return reverse('courses:detail_view', args=[id])

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        obj = self.get_object()
        context['course'] = obj
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.updated_by = self.current_user
        obj.save()

        return redirect(self.success_url)

    def post(self, request, pk):
        current_user = request.user if request.user else None
        course = get_object_or_404(Course, id=pk)
        form = self.form_class(request.POST, request.FILES, instance=course)
        if form.is_valid() and not current_user.is_anonymous:
            form.cleaned_data['created_by'] = course.created_by
            form.cleaned_data['updated_by'] = current_user
            form.save()
            messages.info(request, 'Курс обновлен!')
            return redirect(self.get_detail_url(course.id))
        return render(request, 'courses/update.html', context={'form': form, 'course': course})


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/admin/'
    model = Course
    template_name = "courses/delete.html"

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        obj = self.get_object()
        context['course'] = obj
        return context

    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        messages.error(request, 'Курс удален!')
        return redirect(reverse('courses:index'))


def handler404(request, exception):
    return render(request, '404.html', locals())
