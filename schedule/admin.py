from django.contrib import admin

from courses.admin import get_app_list
from .models import Group, List, Membership, Personal

from django.db import models
from django.contrib.admin.widgets import AdminDateWidget


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


class MembershipInline(admin.TabularInline):
    model = Group.members.through
    extra = 1


class PersonalInline(admin.TabularInline):
    model = Group.teachers.through
    extra = 1


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'course', 'created_by', 'updated_by']
    list_display_links = ['name']
    list_filter = ['course']
    exclude = ['created_by', 'updated_by', 'members', 'teachers']
    inlines = [MembershipInline, PersonalInline]

    def save_model(self, request, obj, form, change):
        current_user = request.user
        if obj.id is None:
            obj.created_by = current_user
        if form.changed_data:
            obj.updated_by = current_user
        obj.save()


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'lesson', 'get_teacher', 'group', 'started_at', 'ended_at',
                    'created_by', 'updated_by']
    list_display_links = ['course']
    list_filter = ['course', 'teacher', 'group', 'started_at', 'ended_at']
    exclude = ['created_by', 'updated_by']

    formfield_overrides = {
        models.DateField: {'widget': AdminDateWidget},
    }

    def get_teacher(self, obj):
        return obj.teacher.get_full_name()

    def save_model(self, request, obj, form, change):
        current_user = request.user
        if obj.id is None:
            obj.created_by = current_user
        if form.changed_data:
            obj.updated_by = current_user
        obj.save()

    get_teacher.short_description = 'Преподаватель'


admin.AdminSite.get_app_list = get_app_list
