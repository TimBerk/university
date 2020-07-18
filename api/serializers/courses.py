from rest_framework import serializers

from api.serializers.categories import CategoryListSerializer
from api.serializers.lessons import LessonListSerializer
from courses.models import Course


class CourseListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ('name', 'slug', 'category')


class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(read_only=True)
    lesson_course = LessonListSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        exclude = ('created_by', 'updated_by', 'status')


class CourseCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        exclude = ('created_by', 'updated_by',)
