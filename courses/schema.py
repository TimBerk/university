import graphene

from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from courses.models import Category, Course, Lesson, Task


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class CourseType(DjangoObjectType):
    class Meta:
        model = Course


class CourseFilteredType(DjangoObjectType):
    class Meta:
        model = Course
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (graphene.relay.Node, )


class LessonType(DjangoObjectType):
    class Meta:
        model = Lesson


class TaskType(DjangoObjectType):
    class Meta:
        model = Task


class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    all_courses = graphene.List(CourseType)
    all_lessons = graphene.List(LessonType)
    all_tasks = graphene.List(TaskType)

    filtered_course = DjangoFilterConnectionField(CourseFilteredType)

    retrieve_course = graphene.Field(CourseType, id=graphene.Int())

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_courses(self, info, **kwargs):
        if 'limit' in kwargs:
            return Course.objects.all()[:kwargs['limit']]
        return Course.objects.select_related('category').all()

    def resolve_all_lessons(self, info, **kwargs):
        if 'limit' in kwargs:
            return Lesson.objects.all()[:kwargs['limit']]
        return Lesson.objects.select_related('course').all()

    def resolve_all_tasks(self, info, **kwargs):
        if 'limit' in kwargs:
            return Task.objects.all()[:kwargs['limit']]
        return Task.objects.select_related('lesson').all()

    def resolve_retrieve_course(self, info, **kwargs):
        if 'id' in kwargs:
            return Course.objects.get(id=kwargs['id'])


schema = graphene.Schema(query=Query)
