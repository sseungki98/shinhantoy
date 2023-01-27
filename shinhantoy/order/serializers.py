from rest_framework import serializers
from .models import Order, Comment

class OrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    member_username = serializers.SerializerMethodField()
    tstamp = serializers.DateTimeField(
        read_only=True, format='%Y-%m-%d %H:%M:%S'
    )

    def get_member_username(self, obj):
        return obj.member.username

    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer):
    member = serializers.HiddenField(
        default = serializers.CurrentUserDefault(),
        required=False
    )

    def validate_member(self, value):
        if not value.is_authenticated:
            raise serializers.ValidationError("Login is required")
        return value

    class Meta:
        model = Comment
        fields = '__all__'

class CommentDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'