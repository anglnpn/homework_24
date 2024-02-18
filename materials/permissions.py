from rest_framework.permissions import BasePermission


class IsModer(BasePermission):
    """
    Проверка на модератора
    """
    def has_permission(self, request, view):
        if request.user.is_staff:
            return request.user.groups.filter(name='moderator').exists()
        else:
            return False


class IsAuthor(BasePermission):
    """
    Проверка на автора курса и урока
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author

