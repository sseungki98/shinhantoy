from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import Member

class MemberRegistSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError('Too short Password, Over 6 Plz')
        return make_password(value)

    def validate_username(self, value):
        if Member.objects.filter(username=value).exists():
            raise serializers.ValidationError("Already exist username")
        return value

    class Meta:
        model = Member
        fields = ('id', 'username', 'tel', 'password')
        extra_kwargs = {
            'id': {
                'read_only': True,
            },
            'password': {
                'write_only': True
            }
        }

class ChangePasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = "__all__"
