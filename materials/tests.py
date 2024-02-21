from rest_framework.test import APITestCase, force_authenticate
from rest_framework import status

from materials.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(name='Test', surname='Test', email='test@t.com', is_superuser=True)
        self.course = Course.objects.create(name_course='Course Name', description='Course Description')
        self.lesson = Lesson.objects.create(name_lesson='Lesson Name', description='List Description',
                                            link='https://my.sky.pro/youtube.com', course_id=self.course,
                                            author=self.user)

    def test_create_lesson(self):
        """
        Тестирование создания урока
        """
        data = {
            'name_lesson': 'Test',
            'description': 'Test',
            'link': 'https://my.sky.pro/youtube.com',
            'course_id': self.course.id,
            'author': self.user.id
        }
        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            '/lesson/create/',
            data=data
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_lesson(self):
        """
        Тестирование просмотра списка уроков
        """

        response = self.client.get(
            '/lesson/'
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_lesson(self):
        """
        Тестирование просмотра одного урока
        """

        self.client.force_authenticate(user=self.user)
        print(self.lesson.id)

        response = self.client.get(
            f'/lesson/{self.lesson.id}/'
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_lesson(self):
        """
        Тестирование изменения списка уроков
        """

        data = {
            "name_lesson": "test4555",
            "link": "https://youtube.com",
            "description": "uuid",
            "course_id": self.course.id
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.put(
            f'/lesson/update/{self.lesson.id}/',
            data=data
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """
        Тестирование удаление урока
        """

        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            f'/lesson/delete/{self.lesson.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Lesson.objects.filter(id=self.lesson.id).exists()
        )


class ClassTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(name='Test', surname='Test', email='test@t.com', is_superuser=True)
        self.course = Course.objects.create(name_course='Course Name', description='Course Description')
        self.lesson = Lesson.objects.create(name_lesson='Lesson Name', description='List Description',
                                            link='https://my.sky.pro/youtube.com', course_id=self.course,
                                            author=self.user)

    def test_create_course(self):
        """
        Тестирование создания курса
        """
        data = {
            'name_course': 'Test',
            'description': 'Test',
            'author': self.user.id
        }
        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            '/course/create/',
            data=data
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_course(self):
        """
        Тестирование просмотра списка курсов
        """

        response = self.client.get(
            '/'
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_course(self):
        """
        Тестирование просмотра одного курса
        """

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            f'/course/{self.course.id}/'
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_course(self):
        """
        Тестирование изменения списка курсов
        """

        data = {
            "name_course": "Test2",
            "description": "test",
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.put(
            f'/course/update/{self.course.id}/',
            data=data
        )
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_course(self):
        """
        Тестирование удаление курса
        """

        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            f'/course/delete/{self.course.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
