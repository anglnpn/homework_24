from datetime import timezone, datetime

from rest_framework import generics

from materials.models import Course, Lesson
from materials.paginators import MaterialsPagination
from materials.permissions import IsModer, IsAuthor
from materials.serializers import CourseSerializer, LessonSerializer, CourseListSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from materials.tasks import send_moderator_email


class CourseCreateAPIView(generics.CreateAPIView):
    """
    Создание курса
    """

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, ~IsModer]

    # permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CourseListAPIView(generics.ListAPIView):
    """
    Вывод списка курсов
    """
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    pagination_class = MaterialsPagination

    def get(self, request):
        queryset = Course.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = CourseListSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного курса
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsAuthor]
    # permission_classes = [AllowAny]


class CourseUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение курса
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsAuthor]


class CourseDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление курса
    """
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor]
    # permission_classes = [AllowAny]


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Cоздание урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsModer]

    # permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    """
    Просмотр списка уроков
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsAuthor]
    # permission_classes = [AllowAny]
    pagination_class = MaterialsPagination

    def get(self, request):
        queryset = Lesson.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = LessonSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsAuthor]
    # permission_classes = [AllowAny]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsAuthor]

    # permission_classes = [AllowAny]

    def perform_update(self, serializer):
        """
        Получает id курса из данных урока.
        Вызывает функцию send_moderator_email.
        """
        serializer.save()
        data = self.request.data
        # получаем id курса из данных
        course_id = data.get('course_id')

        # получаем объект курса
        course_obj = Course.objects.get(id=course_id)

        # обновляем дату изменения курса
        course_obj.update_date = datetime.utcnow()
        course_obj.save()

        # вызываем задачу для отправки письма
        send_moderator_email(course_id)


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление уроков
    """
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor, ~IsModer]
    # permission_classes = [AllowAny]
