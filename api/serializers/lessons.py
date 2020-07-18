from rest_framework import serializers

from courses.models import Lesson
from api.serializers.tasks import TaskListSerializer


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'name', 'slug', 'description')


class LessonDetailSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    task_lesson = TaskListSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        exclude = ('created_by', 'updated_by',)


class LessonCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        exclude = ('created_by', 'updated_by',)
