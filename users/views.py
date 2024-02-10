from rest_framework import viewsets, generics, filters

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from users.models import User, Payments
from users.serializers import UserSerializer, PaymentsSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Представление пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateAPIView(generics.CreateAPIView):
    """
    Cоздание пользователя
    """
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    """
    Просмотр списка уроков
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление пользователя
    """
    queryset = User.objects.all()


class PaymentsListAPIView(generics.ListAPIView):
    """
    Вывод списка платежей.
    Подключена фильтрация по курсу, способу оплаты
    и дате.
    """
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['payment_course']
    search_fields = ['payment_method']
    ordering_fields = ['payment_date']
