from rest_framework import serializers

from courses.models import Task


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'max_mark', 'lesson')


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
