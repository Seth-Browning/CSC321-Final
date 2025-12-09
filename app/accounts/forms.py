from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exclude(pk= self.instance.pk).exists():
            raise forms.ValidationError("This username is already taken.")
        return username