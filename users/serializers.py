from rest_framework import serializers

from users.models import User, Payments, Subscribe


class PaymentsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для платежей
    """

    class Meta:
        model = Payments
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для пользователя
    """

    payments = PaymentsSerializer(source='payments_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = ['password', 'name', 'surname', 'age', 'email', 'phone', 'avatar', 'city', 'payments']


class LimitedUserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для пользователя, вывод только определенных полей
    """

    class Meta:
        model = User
        fields = ['name', 'age', 'avatar', 'city']


class SubscribeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для подписки
    """

    class Meta:
        model = Subscribe
        fields = '__all__'
