from rest_framework import viewsets, status, views, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Movie, Review
from .serializers import UserSerializer, MovieSerializer, ReviewSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_auth.registration.views import RegisterView
from django.core.exceptions import ObjectDoesNotExist

import datetime
import uuid


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'delete', 'put']
    permission_classes = (AllowAny,)

    @action(detail=True, methods=['DELETE'])
    def delete_user(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
            username = user.username
            user.delete()
            response = {'message': username + " has been deleted"}
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            response = {'message': e.args}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        response = {'message': "Please use the provided api/users/delete_user [DELETE] method"}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


class MovieViewSet(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_class = (AllowAny, )

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'rating' in request.data:

            movie = Movie.objects.get(id=pk)
            rating = request.data['rating']
            review = request.data['review']
            user = request.user
            current_time = datetime.datetime.now()

            try:
                # update the review
                review_data = Review.objects.get(user=user.id, movie=movie.id)
                review_data.rating = rating
                review_data.review = review
                review_data.updated_at = current_time
                review_data.save()
                serializer = ReviewSerializer(rating, many=False)
                response = {'message': 'Review updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                # if record not exist that create a new one
                review_data = Review.objects.create(user=user, movie=movie, rating=rating, review=review,
                                                    created_at=current_time, updated_at=current_time)
                serializer = ReviewSerializer(rating, many=False)
                response = {'message': 'Review created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'You need to provide review'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant update rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You cant create rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
