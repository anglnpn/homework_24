from rest_framework import viewsets, generics, filters

from django_filters.rest_framework import DjangoFilterBackend

from users.models import User, Payments
from users.permissions import IsUser
from users.serializers import UserSerializer, PaymentsSerializer, LimitedUserSerializer

from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    """
    Представление пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserCreateAPIView(generics.CreateAPIView):
    """
    Cоздание пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListAPIView(generics.ListAPIView):
    """
    Просмотр списка пользователей
    """
    queryset = User.objects.all()
    serializer_class = LimitedUserSerializer
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного пользователя
    """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return UserSerializer
        else:
            return LimitedUserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsUser]


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление пользователя
    """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsUser]


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
    permission_classes = [IsAuthenticated, IsUser]
