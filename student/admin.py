from django.contrib import admin

from courses.admin import get_app_list
from student.models import Homework

ADMIN_ORDERING = [
    ('auth', [
        'Group',
        'User',
    ]),
    ('user', [
        'Profile',
        'Scope',
        'Skill'
    ]),
    ('courses', [
        'Category',
        'Course',
        'Lesson',
        'Task',
        'TaskCriteria',
    ]),
    ('schedule', [
        'Group',
        'List',
    ]),
    ('student', [
        'Homework'
    ]),
]


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_full_user', 'task',  'score', 'status', 'teacher']
    list_display_links = ['get_full_user']
    list_filter = ['user', 'score']
    exclude = ['created_by', 'updated_by']

    def get_full_user(self, obj):
        return obj.user.get_full_name()

    def teacher(self, obj):
        return obj.created_by.get_full_name()

    def save_model(self, request, obj, form, change):
        current_user = request.user
        if obj.id is None:
            obj.created_by = current_user
        if form.changed_data:
            obj.updated_by = current_user
        obj.save()

    get_full_user.short_description = 'Студент'
    teacher.short_description = 'Преподаватель'


admin.AdminSite.get_app_list = get_app_list
