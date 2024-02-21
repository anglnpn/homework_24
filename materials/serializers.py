from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import MaterialLinkCustomValidator
from users.models import Subscribe
from users.serializers import SubscribeSerializer


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [MaterialLinkCustomValidator(field='link')]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, instance):
        return instance.lesson_set.count()


class CourseListSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    subscribe = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'name_course', 'lessons_count', 'subscribe']

    def get_lessons_count(self, instance):
        return instance.lesson_set.count()

    def get_subscribe(self, instance):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            user = request.user
            if Subscribe.objects.filter(course=instance, user=user).exists():
                return 'У вас есть подписка'
        return 'У вас нет подписки'
