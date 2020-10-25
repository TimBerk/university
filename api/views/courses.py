from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import api_view, permission_classes


from courses.models import Course, STATUS_ACTIVE
from api.serializers.courses import (
    CourseListSerializer,
    CourseDetailSerializer,
    CourseCreateSerializer
)

from api.permissions import IsOwnerUser
from rest_framework.response import Response
from schedule.models import Group


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(status=STATUS_ACTIVE)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        if self.action == 'create':
            return CourseCreateSerializer
        return CourseListSerializer

    def get_permissions(self):
        if self.action in ['update', 'delete']:
            return [IsOwnerUser()]
        elif self.action == 'create':
            return [IsAdminUser()]
        else:
            return [AllowAny()]


class UserCourses(generics.ListAPIView):
    serializer_class = CourseListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        user_groups = user.membership_set.values_list('member_id', flat=True)
        queryset = Course.objects.filter(schedule_course__group__members__in=user_groups).distinct()
        return queryset


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def join_to_course(request, pk):
    course_id = pk
    user = request.user
    if user.is_anonymous:
        return Response({'data': 'Только авторизованный пользователь может поступить на курс'})

    last_group = Group.objects.filter(course_id=course_id).order_by('-schedule_group__course__started_at').first()
    if last_group is None:
        return Response({'data': 'Набор на курс закрыт'})

    user_groups = last_group.members.distinct().values_list('group_members__members__id', flat=True)
    if user.id in user_groups:
        return Response({'data': 'Вы уже записаны на этот курс'})

    last_group.members.add(user)
    last_group.save()
    return Response({'data': 'Вы  записались курс'})
