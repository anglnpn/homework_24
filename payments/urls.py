from django.urls import path

from payments.apps import PaymentsConfig

from payments.views import PaymentsListAPIView, SubscribeCreateAPIView, PaymentsCreateAPIView


app_name = PaymentsConfig.name


urlpatterns = [
    path('list/', PaymentsListAPIView.as_view(), name='payment_list'),
    path('subscribe_create/', SubscribeCreateAPIView.as_view(), name='subscribe'),
    path('payment_create/', PaymentsCreateAPIView.as_view(), name='payments'),
              ]
