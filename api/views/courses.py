from rest_framework import viewsets

from courses.models import Course, STATUS_ACTIVE
from api.serializers.courses import (
    CourseListSerializer,
    CourseDetailSerializer,
    CourseCreateSerializer
)

from api.permissions import IsOwnerUser


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(status=STATUS_ACTIVE)
    permission_classes = [IsOwnerUser]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        if self.action == 'create':
            return CourseCreateSerializer
        return CourseListSerializer
