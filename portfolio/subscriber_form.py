from django import forms
from portfolio.models import Subscriber


class SubscribeForm(forms.ModelForm):
    is_subscribe = forms.BooleanField

    class Meta():
        model = Subscriber
        fields = ('email', 'is_subscribe')
        widgets = {'is_subscribe': forms.HiddenInput(), 'email': forms.EmailInput()}

        labels = {
            'is_subscribe': 'Is Subscribe ?',
            'email': 'Email Address'
        }

        error_messages = {
            'email': {
                'required': "Email Field is mandatory.",
            },
        }
