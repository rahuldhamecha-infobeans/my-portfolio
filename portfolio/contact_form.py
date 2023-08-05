from django import forms
from portfolio.models import Contact


class ContactForm(forms.ModelForm):
    email = forms.EmailInput()

    class Meta():
        model = Contact
        fields = ('name','email','subject','message')

        labels = {
            'name': 'Name',
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message'
        }

        error_messages = {
            'name': {
                'required': "Name Field is mandatory.",
                'max_length' : 'Name field should max 256 character long.'
            },
            'email': {
                'required' : 'Email Field is mandatory.',
                'max_length': 'Email field should max 256 character long.'
            },
            'subject': {
                'required': "Subject Field is mandatory.",
                'max_length': 'Subject field should max 1000 character long.'
            },
            'message': {
                'required': "Message Field is mandatory.",
            },

        }
