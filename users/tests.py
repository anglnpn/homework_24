from rest_framework.test import APITestCase, force_authenticate
from rest_framework import status

from materials.models import Course, Lesson
from users.models import User


class SubscribeTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(name='Test', surname='Test', email='test@t.com', is_superuser=True)
        self.course = Course.objects.create(name_course='Course Name', description='Course Description')

    def test_create_subscribe(self):
        """
        Тестирование создания подписки
        """
        data = {
            'course_id': self.course.id
        }

        self.client.force_authenticate(user=self.user)

        response_create = self.client.post(
            '/user/subscribe/',
            data=data
        )

        response_delete = self.client.post(
            '/user/subscribe/',
            data=data
        )

        print(response_create.json())

        self.assertEqual(
            response_create.status_code,
            status.HTTP_200_OK
        )

        print(response_delete.json())

        self.assertEqual(
            response_delete.status_code,
            status.HTTP_200_OK
        )



