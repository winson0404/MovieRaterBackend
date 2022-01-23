from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Movie(models.Model):
    name = models.TextField(null=False, max_length=32)
    director = models.TextField(null=False, max_length=32)
    casts = models.TextField(null=False)
    description = models.TextField(null=False)
    duration = models.TextField(null=False)
    aired_at = models.DateTimeField(auto_now_add=False)
    image_url = models.URLField(default="https://i.kym-cdn.com/entries/icons/original/000/020/002/memeeman.jpg")

    def no_of_reviews(self):
        reviews = Review.objects.filter(movie=self)
        return len(reviews)

    def avg_rating(self):
        sum = 0
        ratings = Review.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.rating

        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    review = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)

