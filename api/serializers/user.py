from django.contrib.auth import authenticate, login

from rest_framework.authtoken.models import Token
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
        fields = ('username', 'email', 'profile', 'first_name', 'last_name')


class StudentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    queryset = User.objects.filter(groups__name='student')

    class Meta:
        model = User
        fields = ('username', 'email', 'profile', 'first_name', 'last_name')


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
        fields = ('username', 'email', 'profile', 'first_name', 'last_name')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError('Login требуется для входа в систему.')

        if password is None:
            raise serializers.ValidationError('Для входа в систему требуется пароль.')

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError('Пользователь с таким адресом электронной почты и паролем не найден.')

        if not user.is_active:
            raise serializers.ValidationError('Пользователь не найден.')

        token, created = Token.objects.get_or_create(user=user)

        return {
            'token': token
        }

    def login(self, data, request):
        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)
        login(request, user)
