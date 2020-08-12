from django.contrib.auth.models import User

import graphene
from graphene_django.types import DjangoObjectType

from schedule.models import Group, Membership, List, Personal


class UserType(DjangoObjectType):
    class Meta:
        model = User


class GroupType(DjangoObjectType):
    class Meta:
        model = Group


class MembershipType(DjangoObjectType):
    class Meta:
        model = Membership


class PersonalType(DjangoObjectType):
    class Meta:
        model = Personal


class ListType(DjangoObjectType):
    class Meta:
        model = List
        fields = ("group", "teacher",)


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_groups = graphene.List(GroupType)
    all_members = graphene.List(MembershipType)
    all_personal = graphene.List(PersonalType)
    all_list = graphene.List(ListType)
    teacher = graphene.Field(UserType, id=graphene.Int())

    def resolve_teacher(self, info, **args):
        id = args.get('id')
        if id is not None:
            return User.objects.filter(pk=id).first()

    def resolve_all_groups(self, info, **kwargs):
        return Group.objects.all()

    def resolve_all_members(self, info, **kwargs):
        return List.objects.select_related('group').all()

    def resolve_all_personal(self, info, **kwargs):
        return List.objects.select_related('group').distinct().all()

    def resolve_all_users(self, info, **kwargs):
        return List.objects.select_related('membership').distinct().all()

    def resolve_all_list(self, info, **kwargs):
        return List.objects.select_related('group').all()


schema = graphene.Schema(query=Query)
