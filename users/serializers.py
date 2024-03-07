from rest_framework import serializers

from payments.serializers import PaymentsSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для пользователя
    """

    payments = PaymentsSerializer(source='payments_set',
                                  many=True,
                                  read_only=True)

    class Meta:
        model = User
        fields = ['password',
                  'name',
                  'surname',
                  'age',
                  'email',
                  'phone',
                  'avatar',
                  'city',
                  'payments']


class LimitedUserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для пользователя, вывод только определенных полей
    """

    class Meta:
        model = User
        fields = ['name', 'age', 'avatar', 'city']
