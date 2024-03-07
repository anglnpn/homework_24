from datetime import datetime, timedelta

from celery import shared_task

from users.models import User


@shared_task
def checking_users():
    """
    Проверка пользователей на последний last_login
    Если пользователь не заходил месяц - устанавливается is_active = False
    """
    # Получаем пользователей, которые не логинились месяц
    users = User.objects.filter(
        last_login__lt=datetime.utcnow() - timedelta(days=30),
        is_active=True,
        is_superuser=False,
        is_staff=False
    ).all()

    # Проверяем наличие пользователей
    if users:
        # меняем флаг is_active на False
        for user in users:
            user.is_active = False
            user.save()

        return f'Заблокированы пользователи: ' \
               f'{", ".join(str(user) for user in users)}'
    else:
        return 'Нет пользователей для блокировки'
