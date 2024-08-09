from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        feilds = ['text','photo']
        exclude = ('user',)

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        photo = cleaned_data.get('photo')

        if not text:
            self.add_error('text', 'This field is required.')
        if not photo:
            self.add_error('photo', 'This field is required.')
        

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        exclude = ()
        fields= ('username', 'email', 'password1','password2')