from rest_framework import generics

from courses.models import Course
from api.serializers.courses import (
    CourseListSerializer,
    CourseDetailSerializer,
    CourseCreateSerializer
)

from api.permissions import IsOwnerUser

STATUS_ACTIVE = 1


class CourseListView(generics.ListAPIView):
    serializer_class = CourseListSerializer

    def get_queryset(self):
        courses = Course.objects.filter(status=STATUS_ACTIVE)
        return courses


class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.filter(status=STATUS_ACTIVE)
    serializer_class = CourseDetailSerializer


class CourseCreateView(generics.CreateAPIView):
    serializer_class = CourseCreateSerializer

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(created_by=current_user, updated_by=current_user)


class CourseUpdateView(generics.UpdateAPIView):
    permission_classes = (IsOwnerUser,)
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer

    def perform_update(self, serializer):
        current_user = self.request.user
        serializer.save(updated_by=current_user)
