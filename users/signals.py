from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .models import *

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email = user.email,
        )



def updateProfile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created==False:
        user.username = profile.username
        user.username = profile.username
        user.save()



def deleteProfile(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createProfile, sender=User)
post_save.connect(updateProfile, sender=Profile)
post_delete.connect(deleteProfile, sender=Profile)