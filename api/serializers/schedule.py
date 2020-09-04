from rest_framework import serializers

from api.serializers.courses import CourseSimpleListSerializer
from api.serializers.lessons import LessonSimpleListSerializer
from api.serializers.user import TeacherSimpleSerializer
from api.serializers.group import GroupSimpleListSerializer
from schedule.models import List


class ScheduleListSerializer(serializers.ModelSerializer):
    course = CourseSimpleListSerializer(read_only=True)
    lesson = LessonSimpleListSerializer(read_only=True)
    teacher = TeacherSimpleSerializer(read_only=True)
    group = GroupSimpleListSerializer(read_only=True)

    class Meta:
        model = List
        fields = ('pk', 'course', 'lesson', 'teacher', 'group', 'started_at', 'ended_at')


class ScheduleDetailSerializer(serializers.ModelSerializer):
    course = CourseSimpleListSerializer(read_only=True)
    lesson = LessonSimpleListSerializer(read_only=True)
    teacher = TeacherSimpleSerializer(read_only=True)
    group = GroupSimpleListSerializer(read_only=True)

    class Meta:
        model = List
        exclude = ('created_by', 'updated_by', 'status')


class ScheduleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        exclude = ('created_by', 'updated_by',)
