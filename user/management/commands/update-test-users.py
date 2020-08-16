import os
import json

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from university.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Обновление тестовых профилей'

    def handle(self, *args, **options):
        options.setdefault('interactive', False)
        current_path = os.path.join(BASE_DIR, 'user/fixtures/test-users.json')
        with open(current_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        if len(json_data) > 0:
            for user_data in json_data:
                user = User.objects.get(pk=user_data['pk'])
                user.first_name = user_data['fields']['first_name']
                user.last_name = user_data['fields']['last_name']
                user.save()
