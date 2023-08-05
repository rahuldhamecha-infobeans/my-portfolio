from django import forms
from django.contrib.auth.models import User
from authentication.models import UserProfile
from django.contrib.auth import authenticate

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('profile_pic','social_link')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password','first_name','last_name')

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)

    def clean(self):
        data = super().clean()
        username = data['username']
        password = data['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                pass
            else:
                self.add_error('username','Username or Password Mismatch.')
        else:
            self.add_error('username','Username or Password Mismatch.')

        return data
