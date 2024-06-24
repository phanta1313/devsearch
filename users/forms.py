from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name == 'username':
                field.widget.attrs.update({
                    'class': "input input--text",
                    'id' : "formInput#text",
                    'placeholder' : 'Enter new username',
                })
            if name == 'password1':
                field.widget.attrs.update({
                    'class': "input input--password",
                    'id' : "formInput#passowrd",
                    'placeholder' : 'Create password',
                })
            if name == 'password2':
                field.widget.attrs.update({
                    'class': "input input--password",
                    'id' : "formInput#confirm-passowrd",
                    'placeholder' : 'Confirm password',
                })


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'quick_description', 'bio', 'location', 'profile_image']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input'})

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input'})  

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'subject', 'body']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input'})  

      