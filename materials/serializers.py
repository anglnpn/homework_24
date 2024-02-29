from rest_framework import serializers

from materials.models import Course, Lesson
from materials.services import convert_currencies
from materials.validators import MaterialLinkCustomValidator
from payments.models import Subscribe
from payments.serializers import SubscribeSerializer


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [MaterialLinkCustomValidator(field='link')]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    price_course = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'name_course', 'image', 'description', 'author', 'lessons_count', 'lessons', 'price',
                  'price_course', 'update_date']

    def get_lessons_count(self, instance):
        return instance.lesson_set.count()

    def get_price_course(self, instance):
        return convert_currencies(instance.price)


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
