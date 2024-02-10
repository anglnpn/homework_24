from django.urls import path

from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, \
    UserUpdateAPIView, UserDestroyAPIView, PaymentsListAPIView


app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('user/create/', UserCreateAPIView.as_view(), name='user'),
    path('user/', UserListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_get'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),
    path('payment/', PaymentsListAPIView.as_view(), name='payment_list'),
              ] + router.urls
