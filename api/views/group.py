from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from schedule.models import Group, STATUS_ACTIVE
from api.serializers.group import (
    GroupListSerializer,
    GroupDetailSerializer,
)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.filter(status=STATUS_ACTIVE)
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return GroupDetailSerializer
        return GroupListSerializer
