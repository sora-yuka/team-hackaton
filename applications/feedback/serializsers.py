from rest_framework import serializers
from django.contrib.auth import get_user_model

from applications.feedback.models import Comment, Like, Rating

User = get_user_model()


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Comment
        fields = '__all__'


# class LikeSerializer(serializers.ModelSerializer):
#     owner = serializers.EmailField(required=False)
#
#     class Meta:
#         model = Like
#         fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Rating
        fields = ['rating']


class FanSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username',
            'full_name',
        )

    @staticmethod
    def get_full_name(obj):
        return obj.get_full_name()
