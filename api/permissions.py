from rest_framework import permissions


class IsOwnerUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return request.user == obj.created_by
