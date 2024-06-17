from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import Usr

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_recheck = forms.CharField(label='Re-enter Password', widget=forms.PasswordInput)

    class Meta:
        model = Usr 
        fields = ['usrname', 'name', 'password', 'password_recheck', 'dob', 'phoneno']
    
    def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            password_recheck = cleaned_data.get('password_recheck')

            if password and password_recheck and password != password_recheck:
                raise forms.ValidationError("Passwords do not match. Please re-enter them.")

class LoginForm(forms.Form):
     usrname = forms.CharField()
     password = forms.CharField(widget=forms.PasswordInput)

