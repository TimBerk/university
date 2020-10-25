from datetime import datetime
import json
import pendulum

from django.http import HttpResponse
from rest_framework import viewsets
from django.views.decorators.http import require_http_methods
from django.utils.timezone import utc

from schedule.models import List, STATUS_ACTIVE
from api.serializers.schedule import (
    ScheduleListSerializer,
    ScheduleDetailSerializer,
)


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = List.objects.filter(status=STATUS_ACTIVE)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ScheduleDetailSerializer
        return ScheduleListSerializer


@require_http_methods(["POST"])
def get_list_schedule(request):
    results = []
    try:
        data = json.loads(request.body)
        start = datetime.strptime(data.get('start', False), "%Y-%m-%d %H:%M:%S").replace(tzinfo=utc)
        end = datetime.strptime(data.get('end', False), "%Y-%m-%d %H:%M:%S").replace(tzinfo=utc)
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
            'url': f"/course/{item.course.id}",
            'start': '{:%Y-%m-%d %H:%M:%S}'.format(item.started_at),
            'end': '{:%Y-%m-%d %H:%M:%S}'.format(item.ended_at),
        })
    return HttpResponse(json.dumps(results))
