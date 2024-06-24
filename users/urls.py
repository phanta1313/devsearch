from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.profile, name='profile'),

    path('login/', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('registration/', views.registerUser, name='register'),

    path('myAccount/', views.myAccount, name='myAccount'),
    path('edit-account/', views.editAccount, name='editAccount'),

    path('add-skill/', views.addSkill, name='add-skill'),
    path('update-skill/<str:pk>/', views.updateSkill, name='update-skill'),
    path('delete-skill/<str:pk>/', views.deleteSkill, name='delete-skill'),

    path('inbox/', views.inbox, name='inbox'),
    path('send-message/<str:pk>', views.sendMessage, name='send-message')
    
]