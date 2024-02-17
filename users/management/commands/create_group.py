from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    """
    Команда для создания группы модераторов
    """

    def handle(self, *args, **kwargs):
        moderator_group, created = Group.objects.get_or_create(name='moderator')
        if created:
            self.stdout.write(self.style.SUCCESS('Группа модераторов создана'))
        else:
            self.stdout.write(self.style.WARNING('Такая группа уже существует'))
