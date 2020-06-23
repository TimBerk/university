from django.contrib import admin

from .models import Category, Course, Lesson, Task, TaskCriteria

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
]


# Sort function for models in app
def get_app_list(self, request):
    app_dict = self._build_app_dict(request)
    for app_name, object_list in ADMIN_ORDERING:
        app = app_dict[app_name]
        app['models'].sort(key=lambda x: object_list.index(x['object_name']))
        yield app


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'order', 'created_by', 'updated_by']
    list_display_links = ['name']
    exclude = ['created_by', 'updated_by']

    def save_model(self, request, obj, form, change):
        current_user = request.user
        if obj.id is None:
            obj.created_by = current_user
        if form.changed_data:
            obj.updated_by = current_user
        obj.save()


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'order', 'started_at', 'finished_at']
    list_display_links = ['name']
    list_filter = ['category', 'started_at', 'order']
    exclude = ['created_by', 'updated_by']

    def save_model(self, request, obj, form, change):
        current_user = request.user
        if obj.id is None:
            obj.created_by = current_user
        if form.changed_data:
            obj.updated_by = current_user
        obj.save()


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'course', 'order']
    list_display_links = ['name']
    list_filter = ['course', 'order']
    exclude = ['created_by', 'updated_by']

    def save_model(self, request, obj, form, change):
        current_user = request.user
        if obj.id is None:
            obj.created_by = current_user
        if form.changed_data:
            obj.updated_by = current_user
        obj.save()


class TaskCriteriaInline(admin.TabularInline):
    model = TaskCriteria
    exclude = ['created_by', 'updated_by']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'lesson', 'max_mark']
    list_display_links = ['name']
    list_filter = ['lesson', 'max_mark']
    exclude = ['created_by', 'updated_by']
    inlines = [TaskCriteriaInline]

    def save_model(self, request, obj, form, change):
        current_user = request.user
        if obj.id is None:
            obj.created_by = current_user
        if form.changed_data:
            obj.updated_by = current_user
        obj.save()

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        current_user = request.user
        for instance in instances:
            if instance.id is None:
                instance.created_by = current_user
            if form.changed_data or instance.id is None:
                instance.updated_by = current_user
            instance.save()
        formset.save()


@admin.register(TaskCriteria)
class TaskCriteriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'task', 'max_mark']
    list_display_links = ['name']
    list_filter = ['task', 'max_mark']
    exclude = ['created_by', 'updated_by']

    def save_model(self, request, obj, form, change):
        current_user = request.user
        if obj.id is None:
            obj.created_by = current_user
        if form.changed_data:
            obj.updated_by = current_user
        obj.save()


admin.AdminSite.get_app_list = get_app_list
