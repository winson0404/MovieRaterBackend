from django.urls import path
from rest_framework import routers
from django.conf.urls import include, url
# from rest_framework.decorators import schema

from .views import UserViewSet, MovieViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('movies', MovieViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration', include('rest_auth.registration.urls'))
]
