from rest_framework import viewsets, generics, filters

from django_filters.rest_framework import DjangoFilterBackend

from materials.models import Course
from users.models import User, Payments, Subscribe
from users.paginators import UserPagination
from users.permissions import IsUser
from users.serializers import UserSerializer, PaymentsSerializer, LimitedUserSerializer, SubscribeSerializer

from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.hashers import make_password

from rest_framework.views import APIView

from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class UserCreateAPIView(generics.CreateAPIView):
    """
    Cоздание пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        # Хэширование пароля перед сохранением пользователя
        validated_data = serializer.validated_data
        password = validated_data.get('password')
        hashed_password = make_password(password)
        serializer.save(password=hashed_password)


class UserListAPIView(generics.ListAPIView):
    """
    Просмотр списка пользователей
    """
    queryset = User.objects.all()
    serializer_class = LimitedUserSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = UserPagination

    def get(self, request):
        queryset = User.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = LimitedUserSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


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


class SubscribeCreateAPIView(generics.CreateAPIView):
    """
    Cоздание подписки
    """
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course_id')
        course_item = get_object_or_404(Course, id=course_id)

        # Получаем объект подписки по пользователю курсу
        subs_item = Subscribe.objects.filter(user=user, course=course_item)

        # Если подписка у пользователя на этот курс есть - удаляем ее
        if subs_item:
            subs_item.delete()
            message = 'подписка удалена'
        # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            subscribe_new = Subscribe.objects.create(user=user, course=course_item)
            subscribe_new.save()
            message = 'подписка добавлена'
        # Возвращаем ответ в API
        return Response({"message": message})
