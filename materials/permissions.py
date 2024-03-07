from rest_framework.permissions import BasePermission

from payments.models import Payments


class IsModer(BasePermission):
    """
    Проверка на модератора
    """

    def has_permission(self, request, view):
        if request.user.is_staff:
            return request.user.groups.filter(name='moderator').exists()
        else:
            return False


class IsModerPayment(BasePermission):
    """
    Проверка на модератора оплат
    """

    def has_permission(self, request, view):
        if request.user.is_staff:
            return request.user.groups.filter(name='moderator_payment').exists()
        else:
            return False


class IsAuthor(BasePermission):
    """
    Проверка на автора курса и урока
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class IsContributor(BasePermission):
    """
    Проверка, что оплата принадлежит пользователю
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.payment_user


