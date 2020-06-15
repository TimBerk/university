from django.contrib import admin
from django.contrib.auth.models import User
from .models import Scope, Skill, Profile


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'status']
    list_display_links = ['name']
    ordering = ['name']
    exclude = ['created_by', 'updated_by']
    search_fields = ['name']

    def save_model(self, request, obj, form, change):
        current_user = request.user
        if obj.id is None:
            obj.created_by = current_user
        if form.changed_data:
            obj.updated_by = current_user
        obj.save()


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    exclude = ['created_by', 'updated_by']
    search_fields = ['name']

    def save_model(self, request, obj, form, change):
        current_user = request.user
        if obj.id is None:
            obj.created_by = current_user
        if form.changed_data:
            obj.updated_by = current_user
        obj.save()


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = User
    list_display = ['id', 'get_username', 'get_full_name', 'get_email', 'get_phone']
    list_display_links = ['get_username']
    autocomplete_fields = ['skills']

    def get_username(self, obj):
        return obj.user.username

    def get_full_name(self, obj):
        return obj.user.get_full_name()

    def get_email(self, obj):
        return obj.user.email

    def get_phone(self, obj):
        return obj.phone

    get_username.short_description = 'Логин'
    get_full_name.short_description = 'Фамилия и имя'
    get_email.short_description = 'E-mail'

    get_phone.short_description = 'Телефон'
    get_phone.empty_value_display = 'Не указан'
