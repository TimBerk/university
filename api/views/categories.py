from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from courses.models import Category

from api.serializers.categories import (
    CategoryListSerializer,
    CategoryDetailSerializer,
    CategoryCreateSerializer
)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class CategoryCreateView(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = CategoryCreateSerializer

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(created_by=current_user, updated_by=current_user)


class CategoryUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

    def perform_update(self, serializer):
        current_user = self.request.user
        serializer.save(updated_by=current_user)
