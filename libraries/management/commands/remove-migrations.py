import os

from django.core.management.base import BaseCommand

from university.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Удаление файлов миграций'

    def handle(self, *args, **options):
        is_deleted_migrations = False

        for root, folder, files in os.walk(BASE_DIR):
            if 'migrations' in folder:
                migrations_folder = os.path.join(root, 'migrations')
                is_deleted_migration = False
                for file in os.listdir(migrations_folder):
                    if file not in ['__init__.py', '__pycache__']:
                        file_path = os.path.join(migrations_folder, file)
                        os.remove(file_path)
                        is_deleted_migration = True
                if is_deleted_migration:
                    print(f"From folder '{migrations_folder}' deleted migrations")
                if is_deleted_migration and not is_deleted_migrations:
                    is_deleted_migrations = True

        if not is_deleted_migrations:
            print("Migrations not found")
