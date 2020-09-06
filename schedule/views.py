from datetime import datetime
import json
import pendulum

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.utils.timezone import utc

from schedule.models import List, STATUS_ACTIVE


def index_view(request):
    return render(request, 'schedule/index.html')


@require_http_methods(["POST"])
def get_list_schedule(request):
    results = []
    try:
        start = datetime.strptime(request.POST.get('start', False), "%Y-%m-%d %H:%M:%S").replace(tzinfo=utc)
        end = datetime.strptime(request.POST.get('end', False), "%Y-%m-%d %H:%M:%S").replace(tzinfo=utc)
    except ValueError:
        today = pendulum.now()
        start = today.start_of('week')
        end = today.end_of('week')

    data = List.objects.filter(course__status=STATUS_ACTIVE, started_at__gte=start, ended_at__lte=end)\
        .select_related('teacher', 'group', 'course', 'lesson')

    for item in data:
        results.append({
            'groupId': item.course.id,
            'title': item.lesson.name,
            'url': f"/courses/{item.course.id}",
            'start': '{:%Y-%m-%d %H:%M:%S}'.format(item.started_at),
            'end': '{:%Y-%m-%d %H:%M:%S}'.format(item.ended_at),
        })
    return HttpResponse(json.dumps(results))
