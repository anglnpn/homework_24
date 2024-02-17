from django.urls import path

from materials.apps import MaterialsConfig

from materials.views import CourseCreateAPIView, CourseRetrieveAPIView, CourseUpdateAPIView, \
    CourseDestroyAPIView, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, CourseListAPIView

app_name = MaterialsConfig.name

urlpatterns = [
    # курс
    path('course/create/', CourseCreateAPIView.as_view(), name='course_create'),
    path('course/<int:pk>/', CourseRetrieveAPIView.as_view(), name='course_get'),
    path('course/update/<int:pk>/', CourseUpdateAPIView.as_view(), name='course_update'),
    path('course/delete/<int:pk>/', CourseDestroyAPIView.as_view(), name='course_delete'),
    path('course/', CourseListAPIView.as_view(), name='course_list'),
    # урок
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

]
