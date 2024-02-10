from rest_framework import serializers

from users.models import User, Payments


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
        fields = ['name', 'surname', 'age', 'email', 'phone', 'avatar', 'city', 'payments']
