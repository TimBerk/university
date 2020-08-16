from django.contrib.auth.management.commands import createsuperuser
from django.contrib.auth.models import Group, User
from django.core.management import CommandError


class Command(createsuperuser.Command):
    help = 'Создание администратора сайта'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            '--password', dest='password', default=None,
            help='Пароль для администратора',
        )
        parser.add_argument(
            '--group', dest='group', default=None,
            help='Группа пользователя',
        )

    def handle(self, *args, **options):
        options.setdefault('interactive', False)
        database = options.get('database')
        password = options.get('password')
        username = options.get('username')
        email = options.get('email')
        group = options.get('group')

        if not password or not username or not email:
            raise CommandError(
                    "--email --username и --password обязательные поля")

        user_data = {
            'username': username,
            'password': password,
            'email': email,
        }

        if group is None:
            self.UserModel._default_manager.db_manager(database).create_superuser(**user_data)
        else:
            self.UserModel._default_manager.db_manager(database).create_user(**user_data)
            current_user = User.objects.get(username=username)
            teacher_group = Group.objects.get(name='teacher')
            student_group = Group.objects.get(name='student')
            if group == 'teacher':
                teacher_group.user_set.add(current_user.pk)
            elif group == 'student':
                student_group.user_set.add(current_user.pk)

        if options.get('verbosity', 0) >= 1:
            if group is None:
                type_user = 'Администратор'
            elif group == 'teacher':
                type_user = 'Преподаватель'
            elif group == 'student':
                type_user = 'Студент'
            else:
                type_user = 'Пользователь'
            self.stdout.write(f"{type_user} создан успешно.")
