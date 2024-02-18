from rest_framework import viewsets, generics

from materials.models import Course, Lesson
from materials.permissions import IsModer, IsAuthor
from materials.serializers import CourseSerializer, LessonSerializer, CourseListSerializer

from rest_framework.permissions import IsAuthenticated


class CourseCreateAPIView(generics.CreateAPIView):
    """
    Создание курса
    """

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, ~IsModer]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CourseListAPIView(generics.ListAPIView):
    """
    Вывод списка курсов
    """
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    permission_classes = [IsAuthenticated]


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного курса
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsAuthor]


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


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Cоздание урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsModer]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    """
    Просмотр списка уроков
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsAuthor]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsAuthor]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsAuthor]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление уроков
    """
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor, ~IsModer]
