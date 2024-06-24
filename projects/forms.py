from django.forms import ModelForm
from django import forms
from .models import *

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'image', 'description', 'tags']

        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': "input input--text",
                'id' : "formInput#text",
                'type': "text" ,
                'name': "text",
                
            })



class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['body', 'value']
        labels = {
            'value' : 'Place your vote',
            'body' : 'Add a comment with your vote',
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            if name == 'body':
                field.widget.attrs.update({'placeholder' : 'Type a review here...'})