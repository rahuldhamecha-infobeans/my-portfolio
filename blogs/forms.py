from django import forms
from django.contrib.auth.models import User
from blogs.models import Category, Blog
from django.core.exceptions import NON_FIELD_ERRORS


class BlogForm(forms.ModelForm):
    statuses = (
        (True, 'Published'),
        (False, 'Draft')
    )
    content = forms.CharField(widget=forms.Textarea(), error_messages={
        'required': 'Please enter your content.'
    })
    date = forms.DateField(error_messages={
        'required': 'Please select date.'
    },input_formats=['%d-%m-%Y','%Y-%m-%d'])

    class Meta():
        model = Blog
        fields = ('title', 'date', 'content', 'categories', 'status', 'blog_image')

        labels = {
            "status": "Published"
        }

        error_messages = {
            'categories': {
                'required': "Category Field is mandatory.",
            },
            'title': {
                'required': "Title Field is mandatory.",
            },
            'date': {
                'required': "Date Field is mandatory.",
            },
            'content': {
                'required': "Content Field is mandatory.",
            },
            'blog_image': {
                'required': "Featured Image Field is mandatory.",
            },
        }
