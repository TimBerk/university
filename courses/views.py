from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Course


def index_view(request):
    courses = Course.objects.filter(status=1).all()
    context = {
        'courses': courses
    }
    return render(request, 'courses/index.html', context=context)


def detail_view(request, id):
    course = get_object_or_404(Course, pk=id)
    context = {
        'course': course
    }
    return render(request, 'courses/detail.html', context=context)


def handler404(request, exception):
    return render(request, '404.html', locals())
