from rest_framework import serializers

from user.models import Skill, User, Profile


class SkillUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name')


class ProfileSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source='get_gender_display')
    qualification = serializers.CharField(source='get_qualification_display')

    scope = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
    skills = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = Profile
        fields = "__all__"


class UserDetailSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('username', 'email', 'profile')


class StudentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    queryset = User.objects.filter(groups__name='student')

    class Meta:
        model = User
        fields = ('username', 'email', 'profile')


class StudentSimpleSerializer(serializers.ModelSerializer):
    queryset = User.objects.filter(groups__name='student')

    class Meta:
        model = User
        fields = ('pk', 'last_name', 'first_name',)


class TeacherSimpleSerializer(serializers.ModelSerializer):
    queryset = User.objects.filter(groups__name='teacher')

    class Meta:
        model = User
        fields = ('pk', 'last_name', 'first_name',)


class TeacherSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    queryset = User.objects.filter(groups__name='teacher')

    class Meta:
        model = User
        fields = ('username', 'email', 'profile')
