from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from users.models import User


class Command(BaseCommand):
    """
    Команда для добавления пользователя в группу
    """
    def handle(self, *args, **kwargs):
        user_id = 13
        group_name = 'moderator'

        user = User.objects.get(pk=user_id)
        group = Group.objects.get(name=group_name)

        user.groups.add(group)
