from rest_framework import generics, viewsets

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
