from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='index'),
    path('projects/', views.projects, name='projects'),
    path('single-project/<str:pk>/', views.singleProject, name='single-project'),
    path('create-project/', views.createProject, name='create-project'),
    path('update-project/<str:pk>/', views.updateProject, name='update-project'),
    path('delete-project/<str:pk>/', views.deleteProject, name='delete-project'),
]