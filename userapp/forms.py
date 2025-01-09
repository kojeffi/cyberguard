from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        field =  ['username', 'email', 'password1', 'password2']
















class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


     #  Removing helping text  in django forms
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # Remove help_text for all fields
    #     for field_name, field in self.fields.items():
    #         field.help_text = ''


class EmailLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

class UserProfileForm(forms.ModelForm):
    new_password = forms.CharField(widget=forms.PasswordInput, label="Password", required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Password", required=False)

    class Meta:
        model = Profile
        fields = ['profile_photo', 'about', 'age', 'new_password', 'confirm_password']