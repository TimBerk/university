from rest_framework import serializers

from api.serializers.courses import CourseSimpleListSerializer
from api.serializers.user import StudentSimpleSerializer, TeacherSimpleSerializer

from schedule.models import Group, Membership, Personal


class MembershipSerializer(serializers.ModelSerializer):
    member = StudentSimpleSerializer(read_only=True)

    class Meta:
        model = Membership
        fields = ('pk', 'member')


class PersonalSerializer(serializers.ModelSerializer):
    teacher = TeacherSimpleSerializer(read_only=True)

    class Meta:
        model = Personal
        fields = ('pk', 'teacher',)


class GroupSimpleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('pk', 'name',)


class GroupListSerializer(serializers.ModelSerializer):
    course = CourseSimpleListSerializer(read_only=True)

    class Meta:
        model = Group
        exclude = ('created_by', 'updated_by', 'status', 'members', 'teachers')


class GroupDetailSerializer(serializers.ModelSerializer):
    course = CourseSimpleListSerializer(read_only=True)
    members = MembershipSerializer(source='membership_set', many=True, read_only=True)
    teachers = PersonalSerializer(source='personal_set', many=True, read_only=True)

    class Meta:
        model = Group
        exclude = ('created_by', 'updated_by', 'status')
