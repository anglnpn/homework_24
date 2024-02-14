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
    Проверка на автора курса
    """

    def has_permission(self, request, view):
        if request.user == view.get_object().author:
            return True
        else:
            return False
