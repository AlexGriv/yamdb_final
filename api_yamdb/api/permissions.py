from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            request.user.is_authenticated
            and request.user.role == 'admin'
        )


class HasAdminRole(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_superuser
            or (request.user.is_authenticated and request.user.role == 'admin')
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_superuser
            or not (request.user.is_staff and request.data.get('role'))
            or (request.user.is_authenticated and request.user.role == 'admin')
        )


class CommentReviewPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user == obj.author
            or request.user.is_superuser
            or (request.user.is_authenticated
                and request.user.role in ('admin', 'moderator'))
        )
