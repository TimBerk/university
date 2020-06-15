from django.http import HttpResponse


def index_view(request):
    return HttpResponse('<h1>Hello django schedule</h1>')
