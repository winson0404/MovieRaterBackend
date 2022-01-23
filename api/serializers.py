from django.db import transaction
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_auth.registration.serializers import RegisterSerializer
from .models import User, Movie, Review
from .enums import USER_TYPES, MESSAGE_TYPES, SOCIAL_PLATFORMS


# custom register credentials


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "created_at", "updated_at")
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user_id')


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'casts', 'director', 'description', 'no_of_reviews', 'avg_rating', 'duration', 'aired_at', 'image_url')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'rating', 'review', 'user', 'movie', 'created_at', 'updated_at')
