from django.urls import path, include
from . import views

from rest_framework import routers
from .views import ProjectViewSet

router = routers.SimpleRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]