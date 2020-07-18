from rest_framework import serializers

from courses.models import Category


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description')


class CategoryDetailSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Category
        exclude = ('created_by', 'updated_by',)


class CategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('created_by', 'updated_by',)
