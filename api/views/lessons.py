from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from api.permissions import IsOwnerUser

from courses.models import Lesson
from api.serializers.lessons import (
    LessonListSerializer,
    LessonDetailSerializer,
    LessonCreateSerializer
)


class LessonViewSet(viewsets.ViewSet):

    def get_permissions(self):
        if self.action in ['update']:
            return [IsOwnerUser()]
        return super(LessonViewSet, self).get_permissions()

    def list(self, request, pk):
        queryset = Lesson.objects.filter(course__id=pk)
        serializer = LessonListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        current_user = self.request.user
        serializer = LessonCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=current_user, updated_by=current_user)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Lesson.objects.all()
        lesson = get_object_or_404(queryset, pk=pk)
        serializer = LessonDetailSerializer(lesson)
        return Response(serializer.data)

    def update(self, request, pk=None):
        current_user = self.request.user
        queryset = Lesson.objects.all()
        lesson = get_object_or_404(queryset, pk=pk)
        self.check_object_permissions(self.request, lesson)

        serializer = LessonDetailSerializer(
            instance=lesson,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=current_user)
        return Response(serializer.data)
